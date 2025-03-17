:og:description: Django Cheatsheet - Learn the Django basics, the practical way

Cheatsheet
==========

.. title:: Django Cheatsheet - Learn the Django basics, the practical way    
.. meta::
    :description: Complete Django kickOff: models, ORM, forms, context Processors 
    :keywords: django cheatsheet, django tutorial, django forms, django ORM, django models 

`Django <./index.html>`__ is a high-level Python web framework that enables rapid development of secure and maintainable websites. 
Created in 2003 and released in 2005, Django follows the model-template-view (MTV) architectural pattern, which is similar to MVC. 
It emphasizes the DRY (Don't Repeat Yourself) principle and includes everything developers need to build web applications out of the box.

Below is a Django Beginner's Cheatsheet, the core features

.. include::  /_templates/components/banner-top.rst

**Custom Model Managers**

.. code-block:: python

    # models.py
    class PublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    class Article(models.Model):
        # ... other fields ...
        objects = models.Manager()  # Default manager
        published = PublishedManager()  # Custom manager

    # Usage
    Article.published.all()  # Only get published articles


**Model Properties and Methods**

.. code-block:: python    

    from django.utils import timezone

    class Event(models.Model):
        start_date = models.DateTimeField()
        end_date = models.DateTimeField()

        @property
        def is_ongoing(self):
            now = timezone.now()
            return self.start_date <= now <= self.end_date

        def get_duration(self):
            return self.end_date - self.start_date

    # Usage
    event = Event.objects.first()
    if event.is_ongoing:
        print(f"Event duration: {event.get_duration()}")


**Custom Template Tags**

.. code-block:: python    

    # myapp/templatetags/custom_tags.py
    from django import template
    register = template.Library()

    @register.simple_tag
    def get_elapsed_time(date):
        from django.utils import timezone
        delta = timezone.now() - date
        return f"{delta.days} days ago"

    # In template
    {% load custom_tags %}
    <p>Posted {% get_elapsed_time post.created_at %}</p>


**Form Field Customization**

.. code-block:: python    

    # forms.py
    from django import forms

    class RegistrationForm(forms.ModelForm):
        confirm_password = forms.CharField(widget=forms.PasswordInput)

        class Meta:
            model = User
            fields = ['username', 'email', 'password']
            widgets = {
                'password': forms.PasswordInput(),
                'email': forms.EmailInput(attrs={'class': 'form-control'})
            }
            help_texts = {
                'username': 'Letters, digits and @/./+/-/_ only.'
            }


**Custom Context Processors**

.. code-block:: python    

    # context_processors.py
    def site_settings(request):
        return {
            'SITE_NAME': 'My Awesome Site',
            'CONTACT_EMAIL': 'contact@example.com',
            'current_year': datetime.datetime.now().year
        }

    # settings.py
    TEMPLATES = [
        {
            'OPTIONS': {
                'context_processors': [
                    'myapp.context_processors.site_settings',
                ],
            },
        },
    ]

    # Any template can now use these variables
    # {{ SITE_NAME }} {{ CONTACT_EMAIL }}


**Custom Model QuerySets**

.. code-block:: python    

    # models.py
    class ArticleQuerySet(models.QuerySet):
        def published(self):
            return self.filter(status='published')

        def by_category(self, category):
            return self.filter(category__name=category)

    class Article(models.Model):
        objects = ArticleQuerySet.as_manager()

    # Usage
    Article.objects.published().by_category('Technology')


**Django Admin Customization**

.. code-block:: python    

    # admin.py
    from django.contrib import admin

    @admin.register(Article)
    class ArticleAdmin(admin.ModelAdmin):
        list_display = ['title', 'author', 'status', 'created_at']
        list_filter = ['status', 'created_at']
        search_fields = ['title', 'content']
        prepopulated_fields = {'slug': ('title',)}
        date_hierarchy = 'created_at'
        ordering = ['-created_at']

        def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(author=request.user)


**Custom Middleware**

.. code-block:: python    

    # middleware.py
    class SimpleMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            # Code to be executed before view
            request.start_time = time.time()

            response = self.get_response(request)

            # Code to be executed after view
            duration = time.time() - request.start_time
            response['X-Page-Generation-Duration-ms'] = int(duration * 1000)
            return response

    # settings.py
    MIDDLEWARE = [
        'myapp.middleware.SimpleMiddleware',
        # ... other middleware ...
    ]


**Custom Management Commands**

.. code-block:: python    

    # management/commands/cleanup_old_data.py
    from django.core.management.base import BaseCommand

    class Command(BaseCommand):
        help = 'Cleanup old records from database'

        def add_arguments(self, parser):
            parser.add_argument('days', type=int)

        def handle(self, *args, **options):
            cutoff_date = timezone.now() - timedelta(days=options['days'])
            deleted = OldModel.objects.filter(created_at__lt=cutoff_date).delete()
            self.stdout.write(f"Deleted {deleted[0]} records")

    # Usage from terminal
    # python manage.py cleanup_old_data 30


**Signals and Handlers**

.. code-block:: python    

    # signals.py
    from django.db.models.signals import post_save
    from django.dispatch import receiver

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    # apps.py
    class UsersConfig(AppConfig):
        name = 'users'

        def ready(self):
            import users.signals  # noqa

**PRO Tips**

- Use python manage.py shell_plus (Django Extensions) for enhanced shell
- Enable Django Debug Toolbar in development
- Use select_related() and prefetch_related() to optimize queries
- Cache expensive queries using Django's cache framework
- Use F() expressions for database operations
- Create custom template filters for reusable template logic
- Use Django's built-in testing tools


.. include::  /_templates/components/footer-links.rst

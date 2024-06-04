
from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField
from django.utils.text import slugify

# Create your models here.

ROLE_CHOICES = (
    ('admin'   , 'Admin'),
    ('user'    , 'User'),
    ('Company' , 'Company'),
)

def avatar_with_id(instance, filename):
    return "{}/avatar/{}".format(f"{instance.user.id}", filename)

class CategoryChoices(models.TextChoices):
    PROGRAMMING = 'PROGRAMMING', 'Programming'
    FRAMEWORK = 'FRAMEWORK', 'Framework'
    DEPLOYMENT = 'DEPLOYMENT', 'Deployment'
    NOCODE = 'NOCODE', 'No-Code'

class Skills(models.Model):
    category = models.CharField(max_length=100, choices=CategoryChoices.choices)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class JobTypeChoices(models.TextChoices):
    DEVELOPER = 'DEVELOPER', 'Developer'
    TEAMLEADER = 'TEAMLEADER', 'Team Leader'
    DESIGNER = 'DESIGNER', 'Designer'
    DEVOPS = 'DEVOPS', 'DevOps'
    ARCHITECT = 'ARCHITECT', 'Architect'

class Profile(models.Model):
    user      = models.OneToOneField(User, on_delete=models.CASCADE)
    role      = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    full_name = models.CharField(max_length=255, null=True, blank=True)
    country   = models.CharField(max_length=255, null=True, blank=True)
    email     = models.EmailField(max_length=255, null=True, blank=True)
    avatar    = models.ImageField(upload_to=avatar_with_id, null=True, blank=True)
    slug = models.CharField(max_length=255, unique=True, null=True, blank=True)
    trusted = models.BooleanField(default=False)
    public_profile = models.BooleanField(default=False)
    programming_languages = models.ManyToManyField(
        Skills, 
        blank=True, 
        related_name='programming_languages', 
        limit_choices_to={'category': CategoryChoices.PROGRAMMING}
    )
    frameworks = models.ManyToManyField(
        Skills, 
        blank=True,
        related_name='frameworks',  
        limit_choices_to={'category': CategoryChoices.FRAMEWORK}
    )
    deployments = models.ManyToManyField(
        Skills, 
        blank=True, 
        related_name='deployments', 
        limit_choices_to={'category': CategoryChoices.DEPLOYMENT}
    )
    no_codes = models.ManyToManyField(
        Skills, 
        blank=True, 
        related_name='no_codes', 
        limit_choices_to={'category': CategoryChoices.NOCODE}
    )
    bio = QuillField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.slug and self.user.username:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)


class Project(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={'role': 'Company'})
    name = models.CharField(max_length=255)
    description = QuillField(null=True, blank=True)
    technologies = models.ManyToManyField(Skills, related_name='technologies')
    live_demo = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    author = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE, 
        related_name='team', 
        limit_choices_to={'role': 'Company'}
    )
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    members = models.ManyToManyField(
        Profile, 
        blank=True, 
        related_name='members', 
        limit_choices_to={'role': 'user'}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TeamRole(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    author = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE, 
        related_name='team_role', 
        limit_choices_to={'role': 'user'}
    )
    role = models.CharField(max_length=255, choices=JobTypeChoices.choices)


class TeamInvitation(models.Model):
    team = models.ForeignKey(TeamRole, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
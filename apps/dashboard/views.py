import requests
import os
import csv
import re
import uuid
from django.shortcuts import render, redirect, get_object_or_404
from apps.common.models_blog import Article, Bookmark, File, FileType, State, Tag
from django.contrib.auth.decorators import login_required
from apps.blog.forms import ArticleForm
from django.urls import reverse
from django.contrib import messages
from apps.common.models_products import Products
from apps.common.models_authentication import Team, Profile, Project, Skills, RoleChoices
from apps.authentication.forms import DescriptionForm, ProfileForm, CreateProejctForm, CreateTeamForm, SkillsForm
from apps.products.forms import ProductForm, PropsForm
from apps.common.models import Profile, Team, Project, TeamInvitation, JobTypeChoices, TeamRole, Download, Props, CategoryChoices, Event, EventType, GeneratedApp
from apps.payments.models import Purchase
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone
from django.core.paginator import Paginator
from apps.authentication.decorators import role_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta
from django.db.models import Max, Q, Count
from rest_framework.authtoken.models import Token
from django.db.models.functions import TruncDate
from django.utils import timezone
from django.http import HttpResponse, Http404, FileResponse, HttpResponseRedirect
from apps.common.models import FileInfo
from helpers.util import check_input

# Create your views here.

# Blog article
@login_required(login_url='/users/signin/')
def blog_dashboard(request):
    filter_string = {}
    
    search = request.GET.get('search')
    if search:
        # fix hacky inout
        if not check_input(search):
            return HttpResponseRedirect(request.build_absolute_uri('?'))
        
        # use the search string
        filter_string['name__icontains'] = search

    articles = Article.objects.filter(created_by=request.user, **filter_string).order_by('-published_at')

    context = {
        'segment': 'blog_dashboard',
        'parent': 'blog',
        'articles': articles,
        'page_title': "Dashboard - My Articles",
    }
    return render(request, 'dashboard/blog/index.html', context)


@staff_member_required(login_url='/admin/')
def all_blogs(request):
    filter_string = {}

    search = request.GET.get('search')
    if search:
        # fix hacky inout
        if not check_input(search):
            return HttpResponseRedirect(request.build_absolute_uri('?'))
        
        # use the search string
        filter_string['name__icontains'] = search

    articles = Article.objects.filter(**filter_string).order_by('-published_at')

    context = {
        'segment': 'all_articles',
        'parent': 'blog',
        'articles': articles,
        'page_title': "Dashboard - Manage Articles",
    }
    return render(request, 'dashboard/blog/all-blogs.html', context)

@login_required(login_url='/users/signin/')
def bookmarked_blog(request):
    filter_string = {}

    search = request.GET.get('search')
    if search:
        # fix hacky inout
        if not check_input(search):
            return HttpResponseRedirect(request.build_absolute_uri('?'))
        
        # use the search string
        filter_string['name__icontains'] = search

    bookmarked_articles = Bookmark.objects.filter(user=request.user, **filter_string)

    context = {
        'segment': 'bookmarked_blog',
        'parent': 'blog',
        'bookmarked_articles': bookmarked_articles,
        'page_title': "Dashboard - Bookmarked Articles",
    }
    return render(request, 'dashboard/blog/bookmarked-blog.html', context)


@login_required(login_url='/users/signin/')
def delete_blog(request, slug):
    #article = Article.objects.get(slug=slug)
    #article.delete()
    #messages.success(request, 'Blog deleted successfully!')
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/signin/')
def create_blog(request):
    form = ArticleForm(user=request.user)
    tags = Tag.objects.all()
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            data = form.cleaned_data
            article = Article.objects.create(
                title=data.get('title'),
                subtitle=data.get('subtitle'),
                slug=data.get('slug'),
                canonical_url=data.get('canonical_url'),
                visibility=data.get('visibility'),
                featured=data.get('featured') == 'on',
                content=data.get('content'),
                summary=data.get('summary'),
                created_by=request.user
            )

            if thumbnail := data.get('thumbnail'):
                article.thumbnail = File.objects.create(file=thumbnail, created_by=request.user, type=FileType.IMAGE)
            
            if video := data.get('video'):
                article.video = File.objects.create(url=video, created_by=request.user, type=FileType.VIDEO)

            if request.user.profile.trusted or request.user.is_superuser:
                article.state = State.PUBLISHED
                article.published_at = timezone.now()
            else:
                article.state = State.DRAFT

            article.tags.set(data.get('tags'))
            article.save()

            messages.success(request, f"Blog created successfully!")

            return redirect(reverse('update_blog', args=[article.slug]))

    context = {
        'form': form,
        'page_title': "Dashboard - Blog - Write a new Article",
        'segment': 'create_article',
        'parent': 'blog',
        'tags': [{'name': tag.name, 'slug': tag.slug} for tag in tags]
    }
    return render(request, 'dashboard/blog/create-blog.html', context)


@login_required(login_url='/users/signin/')
def update_blog(request, slug):
    article = get_object_or_404(Article, slug=slug)
    initial_data = {
        'title': article.title,
        'content': article.content,
        'summary': article.summary,
        'subtitle': article.subtitle,
        'slug': article.slug,
        'canonical_url': article.canonical_url,
        'tags': article.tags.all(),
        'visibility': article.visibility,
        'featured': article.featured,
        'thumbnail': article.thumbnail,
        'video': article.video.url if article.video else None,
    }
    form = ArticleForm(initial=initial_data, user=request.user)

    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.subtitle = request.POST.get('subtitle')
        article.content = request.POST.get('content')
        article.summary = request.POST.get('summary')
        article.slug = request.POST.get('slug')
        article.canonical_url = request.POST.get('canonical_url')
        article.visibility = request.POST.get('visibility')
        article.featured = request.POST.get('featured') == 'on'

        if thumbnail := request.FILES.get('thumbnail'):
            article.thumbnail = File.objects.create(file=thumbnail, created_by=request.user, type=FileType.IMAGE)
        
        if video := request.POST.get('video'):
            article.video = File.objects.create(url=video, created_by=request.user, type=FileType.VIDEO)

        article.tags.set(request.POST.getlist('tags'))
        article.save()
        messages.success(request, 'Blog updated successfully!')

        if 'preview' in request.POST:
            return redirect(reverse('blog_detail', args=[article.slug]))
        
        return redirect(request.META.get('HTTP_REFERER'))
    
    context = {
        'article': article,
        'form': form,
        'segment': 'blog_dashboard',
        'parent': 'blog',
        'page_title': "Dashboard - Update Article",
    }
    return render(request, 'dashboard/blog/update-blog.html', context)


@login_required(login_url='/users/signin/')
def product_dashboard(request):
    filter_string = {}

    search = request.GET.get('search')
    if search:
        # fix hacky inout
        if not check_input(search):
            return HttpResponseRedirect(request.build_absolute_uri('?'))
        
        # use the search string
        filter_string['name__icontains'] = search

    products = Products.objects.filter(**filter_string)

    context = {
        'products': products,
        'parent': 'products',
        'segment': 'product_dashboard',
        'page_title': 'Dashboard - All Products',
    }
    return render(request, 'dashboard/product/index.html', context)


@login_required(login_url='/users/signin/')
def create_product(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
        'parent': 'products',
        'segment': 'create_product',
        'page_title': 'Dashboard - Create Product',
    }
    return render(request, 'dashboard/product/create.html', context)


@login_required(login_url='/users/signin/')
def update_product(request, slug):
    product =get_object_or_404(Products, slug=slug)
    props = Props.objects.filter(product=product)
    form = ProductForm(instance=product, remove_slug=True)
    props_form = PropsForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product, remove_slug=True)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
        'props_form': props_form,
        'props': props,
        'product': product,
        'parent': 'products',
        'segment': 'product_dashboard',
        'page_title': 'Dashboard - Update Product',
        'categories': CategoryChoices.choices
    }
    return render(request, 'dashboard/product/update.html', context)


@login_required(login_url='/users/signin/')
def delete_product(request, slug):
    #product = Products.objects.get(slug=slug)
    #product.delete()
    #messages.success(request, 'Product deleted successfully!')
    return redirect(request.META.get('HTTP_REFERER'))


# Props
@login_required(login_url='/users/signin/')
def create_props(request):
    if request.method == 'POST':
        form_data = {}
        product_id = request.POST.get('product')
        form_data['product'] = get_object_or_404(Products, pk=product_id)
        for attribute, value in request.POST.items():
            if attribute == 'csrfmiddlewaretoken' or attribute == 'product':
                continue

            if attribute == 'state':
                form_data[attribute] = value == 'on'
            elif attribute == 'order':
                form_data[attribute] = int(value) if value.isdigit() else None
            else:
                form_data[attribute] = value
        
        Props.objects.create(**form_data)

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/signin/')
def update_prop(request, pk):
    prop = get_object_or_404(Props, pk=pk)
    if request.method == 'POST':
        prop.category = request.POST.get('category', prop.category)
        prop.data = request.POST.get('data', prop.data)
        prop.save()

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/signin/')
def delete_prop(request, pk):
    prop = get_object_or_404(Props, pk=pk)
    prop.delete()
    return redirect(request.META.get('HTTP_REFERER'))

# Profile

def is_pro_func(request):
    if request.user.is_authenticated:
        emails = [request.user.profile.email]
        if request.user.email:
            emails.append(request.user.email)

        url = "https://api.gumroad.com/v2/sales"
        one_month_ago = datetime.utcnow() - timedelta(days=30)

        is_pro = False

        for email in emails:
            params = {
                "access_token": getattr(settings, 'GUMROAD_ACCESS_TOKEN'),
                "email": email
            }

            response = requests.get(url, params=params)

            if response.status_code == 200:
                json_response = response.json()
                sales_data = json_response.get('sales', [])
                for sale in sales_data:
                    created_at = datetime.strptime(sale['created_at'], "%Y-%m-%dT%H:%M:%SZ")
                    if created_at > one_month_ago:
                        is_pro = True
                        break
            else:
                print(f"Error: {response.status_code}")
                print(response.text)

            if is_pro:
                break

        return is_pro

    else:
        return False

@login_required(login_url='/users/signin/')
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(instance=profile)
    skill_form = SkillsForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    
    context = {
        'form': form,
        'skill_form': skill_form,
        'parent': 'settings',
        'segment': 'profile',
        'profile': profile,
        'page_title': 'Dashboard - User Profile',
        'is_pro': is_pro_func(request)
    }
    return render(request, 'dashboard/profile.html', context)


@login_required
def regenerate_token(request):
    if request.method == 'POST':
        Token.objects.filter(user=request.user).delete()
        Token.objects.create(user=request.user)
        
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/signin/')
def api_view(request):
    token, _ = Token.objects.get_or_create(user=request.user)
    if request.user.is_superuser:
        events = Event.objects.filter(type=EventType.API)
    else:
        events = Event.objects.filter(type=EventType.API, userId=request.user.pk)
        
    context = {
        'parent': 'settings',
        'segment': 'api',
        'token': token,
        'events': events
    }
    return render(request, 'dashboard/api.html', context)

@staff_member_required(login_url='/admin/')
def stats(request):

    thirty_days_ago = timezone.now() - timezone.timedelta(days=30)

    # Downloads
    downloads_last_30_days = (
        Download.objects.filter(downloaded_at__gte=thirty_days_ago)
        .annotate(date=TruncDate('downloaded_at'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )

    downloads_chart_data = {
        'dates': [entry['date'].strftime('%Y-%m-%d') for entry in downloads_last_30_days],
        'counts': [entry['count'] for entry in downloads_last_30_days],
        'total': Download.objects.count(),
    }

    # Users
    users_last_30_days = (
        User.objects.filter(date_joined__gte=thirty_days_ago)
        .annotate(date=TruncDate('date_joined'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )

    users_chart_data = {
        'dates': [entry['date'].strftime('%Y-%m-%d') for entry in users_last_30_days],
        'counts': [entry['count'] for entry in users_last_30_days],
        'total': User.objects.count(),
    }

    # Generated apps
    generated_apps_last_30_days = (
        GeneratedApp.objects.filter(generated_at__gte=thirty_days_ago)
        .annotate(date=TruncDate('generated_at'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )
    generated_apps_chart_data = {
        'dates': [entry['date'].strftime('%Y-%m-%d') for entry in generated_apps_last_30_days],
        'counts': [entry['count'] for entry in generated_apps_last_30_days],
        'total': GeneratedApp.objects.count(),
    }

    # CSV Processor
    csv_processor_last_30_days = (
        Event.objects.filter(type=EventType.CSV_PROCESS ,created_at__gte=thirty_days_ago)
        .annotate(date=TruncDate('created_at'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )
    csv_processor_chart_data = {
        'dates': [entry['date'].strftime('%Y-%m-%d') for entry in csv_processor_last_30_days],
        'counts': [entry['count'] for entry in csv_processor_last_30_days],
        'total': Event.objects.filter(type=EventType.CSV_PROCESS).count(),
    }

    # DB Migrator
    db_migrator_last_30_days = (
        Event.objects.filter(type=EventType.DB_MIGRATOR ,created_at__gte=thirty_days_ago)
        .annotate(date=TruncDate('created_at'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )
    db_migrator_chart_data = {
        'dates': [entry['date'].strftime('%Y-%m-%d') for entry in db_migrator_last_30_days],
        'counts': [entry['count'] for entry in db_migrator_last_30_days],
        'total': Event.objects.filter(type=EventType.DB_MIGRATOR).count(),
    }

    # DB Processor
    db_processor_last_30_days = (
        Event.objects.filter(type=EventType.DB_PROCESSOR ,created_at__gte=thirty_days_ago)
        .annotate(date=TruncDate('created_at'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )
    db_processor_chart_data = {
        'dates': [entry['date'].strftime('%Y-%m-%d') for entry in db_processor_last_30_days],
        'counts': [entry['count'] for entry in db_processor_last_30_days],
        'total': Event.objects.filter(type=EventType.DB_PROCESSOR).count(),
    }

    # Latest 10 CSV Processed users
    latest_csv_processed_user = (
        Event.objects.filter(type=EventType.CSV_PROCESS)
        .values('userId')
        .annotate(latest_created_at=Max('created_at'))
        .order_by('-latest_created_at')
    )[:5] 

    # Latest 10 DB Migrator users
    latest_db_migrator_user = (
        Event.objects.filter(type=EventType.DB_MIGRATOR)
        .values('userId')
        .annotate(latest_created_at=Max('created_at'))
        .order_by('-latest_created_at')
    )[:5] 

    # Latest 10 DB Processor users
    latest_db_processor_user = (
        Event.objects.filter(type=EventType.DB_PROCESSOR)
        .values('userId')
        .annotate(latest_created_at=Max('created_at'))
        .order_by('-latest_created_at')
    )[:5] 

    context = {
        'page_title': f"Users {User.objects.count()}, Apps {GeneratedApp.objects.count()}, Downloads {Download.objects.count()}", 
        'parent': 'settings',
        'segment': 'stats',
        'downloads_chart_data': downloads_chart_data,
        'users_chart_data': users_chart_data,
        'generated_apps_chart_data': generated_apps_chart_data,
        'csv_processor_chart_data': csv_processor_chart_data,
        'db_migrator_chart_data': db_migrator_chart_data,
        'db_processor_chart_data': db_processor_chart_data,
        'last_generated_apps': GeneratedApp.objects.order_by('-generated_at')[:20],
        'last_downloads': Download.objects.order_by('-downloaded_at')[:20],
        'last_sign_ups': User.objects.order_by('-date_joined')[:20],
        'latest_csv_processed_user': latest_csv_processed_user,
        'latest_db_migrator_user': latest_db_migrator_user,
        'latest_db_processor_user': latest_db_processor_user
    }
    return render(request, 'dashboard/stats.html', context)

def promo(request):
    props = {prop.category: prop.data for prop in Props.objects.all()}
    if request.method == 'POST':
        for attribute, value in request.POST.items():
            if attribute == 'csrfmiddlewaretoken':
                continue

            Props.objects.update_or_create(
                category=attribute,
                defaults={
                    'data': value
                } 
            )
        
        return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'segment': 'promo',
        'props': props
    }
    return render(request, 'dashboard/promo.html', context)

@login_required(login_url='/users/signin/')
def update_skills(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = SkillsForm(request.POST, instance=profile)
        if form.is_valid():
            profile.programming_languages.set(form.cleaned_data.get('programming_languages', []))
            profile.frameworks.set(form.cleaned_data.get('frameworks', []))
            profile.deployments.set(form.cleaned_data.get('deployments', []))
            profile.no_codes.set(form.cleaned_data.get('no_codes', []))
            return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/signin/')
def upload_avatar(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        profile.avatar = request.FILES.get('avatar')
        profile.save()
        messages.success(request, 'Avatar uploaded successfully')
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/signin/')
def delete_account(request):
    request.user.delete()
    return redirect(reverse('signin'))


@login_required(login_url='/users/signin/')
def toggle_profile_role(request):
    profile = get_object_or_404(Profile, user=request.user)
    if profile.role == RoleChoices.USER:
        profile.role = RoleChoices.COMPANY
    else:
        profile.role = RoleChoices.USER

    profile.save()
    return redirect(request.META.get('HTTP_REFERER'))


@role_required(['COMPANY', 'ADMIN'])
def freelancer_list(request):
    freelancers = Profile.objects.filter(role=RoleChoices.USER)
    if not request.user.profile.pro:
        freelancers = freelancers[:25]

    paginator = Paginator(freelancers, 25)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    teams = Team.objects.filter(author__user__pk=request.user.pk)

    context = {
        'parent': 'project_management',
        'segment': 'freelancers',
        'freelancers': page_obj,
        'roles': JobTypeChoices.choices,
        'teams': teams,
        'page_title': 'Dashboard - All Freelancers',
    }
    return render(request, 'dashboard/profile/freelancers.html', context)


def profile_detail(request, username):
    profile = get_object_or_404(Profile, user__username=username)

    context = {
        'profile': profile,
        'page_title': 'Dashboard - Profile Detail ',
    }
    return render(request, 'dashboard/profile/detail.html', context)


@role_required(['COMPANY', 'ADMIN'])
def create_team(request):
    if request.method == 'POST':
        form = CreateTeamForm(request.POST, user=request.user)
        profile = Profile.objects.get(user=request.user)
                
        if not profile.pro and Team.objects.filter(author=profile).count() >= 5:
            messages.error(request, "Non-pro users can only create up to 5 teams.")
            return redirect(request.META.get('HTTP_REFERER'))
        
        if form.is_valid():
            team = form.save(commit=False)
            team.author = profile
            team.save()
            return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))


@role_required(['COMPANY', 'ADMIN'])
def team_list(request):
    filter_string = {}

    search = request.GET.get('search')
    if search:
        # fix hacky inout
        if not check_input(search):
            return HttpResponseRedirect(request.build_absolute_uri('?'))
        
        # use the search string
        filter_string['name__icontains'] = search

    teams = Team.objects.filter(author__user__pk=request.user.pk, **filter_string)
    projects = Project.objects.filter(author__user__pk=request.user.pk)
    if not request.user.profile.pro:
        teams = teams[:5]
        projects = projects[:5]

    paginator = Paginator(teams, 25)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)
    
    form = CreateTeamForm(user=request.user)

    context = {
        'teams': page_obj,
        'parent': 'project_management',
        'segment': 'teams',
        'projects': projects,
        'form': form,
        'page_title': 'Dashboard - My Teams',
    }
    return render(request, 'dashboard/teams/index.html', context)


@role_required(['COMPANY', 'ADMIN'])
def team_detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)

    context = {
        'team': team,
        'parent': 'project_management',
        'segment': 'teams',
        'page_title': f'Team - {team.name}',
    }
    return render(request, 'dashboard/teams/detail.html', context)


@role_required(['COMPANY', 'ADMIN'])
def delete_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    team.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@role_required(['COMPANY', 'ADMIN'])
def edit_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        team.name = request.POST.get('name')
        team.save()
    
    return redirect(request.META.get('HTTP_REFERER'))


@role_required(['COMPANY', 'ADMIN'])
def remove_team_member(request, team_id, profile_id):
    team = get_object_or_404(Team, pk=team_id)
    profile = get_object_or_404(Profile, pk=profile_id)

    team_role = get_object_or_404(TeamRole, team=team, author=profile)
    team_role.delete()

    team.members.remove(profile)
    return redirect(request.META.get('HTTP_REFERER'))


@role_required(['COMPANY', 'ADMIN'])
def create_project(request):
    if request.method == 'POST':
        form = CreateProejctForm(request.POST,user=request.user)
        profile = Profile.objects.get(user=request.user)

        if not profile.pro and Project.objects.filter(author=profile).count() >= 5:
            messages.error(request, "Non-pro users can only create up to 5 projects.")
            return redirect(request.META.get('HTTP_REFERER'))
    
        if form.is_valid():
            project = form.save(commit=False)
            project.author = profile
            project.save()
            project.technologies.set(form.cleaned_data.get('technologies'))
            return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))


@role_required(['COMPANY', 'ADMIN'])
def project_list(request):
    filter_string = {}

    search = request.GET.get('search')
    if search:
        # fix hacky inout
        if not check_input(search):
            return HttpResponseRedirect(request.build_absolute_uri('?'))
        
        # use the search string
        filter_string['name__icontains'] = search

    projects = Project.objects.filter(author__user__pk=request.user.pk, **filter_string)
    if not request.user.profile.pro:
        projects = projects[:5]

    paginator = Paginator(projects, 25)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    technologies = Skills.objects.all()
    description_form = DescriptionForm()
    form = CreateProejctForm(user=request.user)

    context = {
        'projects': page_obj,
        'parent': 'project_management',
        'segment': 'projects',
        'description_form': description_form,
        'technologies': technologies,
        'form': form,
        'page_title': "Dashboard - My Projects",
        
    }
    return render(request, 'dashboard/projects/index.html', context)


@role_required(['COMPANY', 'ADMIN'])
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@role_required(['COMPANY', 'ADMIN'])
def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        project.name = request.POST.get('name')
        # project.description = request.POST.get('description')
        project.live_demo = request.POST.get('live_demo')
        project.technologies.set(request.POST.getlist('technologies'))
        project.save()
    
    return redirect(request.META.get('HTTP_REFERER'))


@role_required(['COMPANY', 'ADMIN'])
def invite_freelancer(request, profile_id):
    if request.method == 'POST':
        profile = get_object_or_404(Profile, pk=profile_id)
        team_role, created = TeamRole.objects.get_or_create(
            author=profile,
            team=get_object_or_404(Team, pk=request.POST.get('team')), 
            defaults={
                'role': request.POST.get('role')
            }
        )
        if created:
            TeamInvitation.objects.create(team=team_role)
        else:
            messages.info(request, "Already invited")

        return redirect(request.META.get('HTTP_REFERER'))
    
    return redirect(request.META.get('HTTP_REFERER'))


@role_required(['USER'])
def invitation_list(request):
    invitations = TeamInvitation.objects.filter(team__author__pk=request.user.pk, accepted=False)

    context = {
        'invitations': invitations,
        'segment': 'invitations',
        'parent': 'project_management',
        'page_title': "Dashboard - My Team Invitations",
    }
    return render(request, 'dashboard/teams/invitations.html', context)


@role_required(['USER'])
def accept_invitations(request, id):
    invitation = TeamInvitation.objects.get(pk=id)
    invitation.accepted = True
    invitation.save()

    team = Team.objects.get(pk=invitation.team.team.pk)
    team.members.add(invitation.team.author)
    team.save()
    return redirect(request.META.get('HTTP_REFERER'))


@role_required(['USER'])
def deny_invitations(request, id):
    invitation = get_object_or_404(TeamInvitation, pk=id)
    team_role = get_object_or_404(TeamRole, pk=invitation.team.pk)
    team_role.delete()
    invitation.delete()

    return redirect(request.META.get('HTTP_REFERER'))


@role_required(['USER'])
def my_projects(request):
    projects = Project.objects.filter(team__members__user__id=request.user.pk)

    context = {
        'projects': projects,
        'parent': 'project_management',
        'segment': 'my_projects',
        'page_title': "Projects",
        'page_title': 'Dashboard - My Projects',
    }
    return render(request, 'dashboard/projects/my-project.html', context)


# Downloads
@login_required(login_url='/users/signin/')
def free_downloads(request):
    latest_downloads = (
        Download.objects
        .filter(user=request.user, product__free=True)
        .values('product')
        .annotate(latest_download_at=Max('downloaded_at'))
    )

    downloads = Download.objects.filter(
        user=request.user, 
        product__free=True,
        downloaded_at__in=[item['latest_download_at'] for item in latest_downloads]
    )

    context = {
        'parent': 'download',
        'segment': 'free_downloads',
        'downloads': downloads,
        'page_title': 'Dashboard - Free Products',
    }
    return render(request, 'dashboard/downloads/free-downloads.html', context)


@login_required(login_url='/users/signin/')
def paid_downloads(request):
    sales = []
    emails = [request.user.profile.email]
    if request.user.email:
        emails.append(request.user.email)

    url = "https://api.gumroad.com/v2/sales"
    for email in emails:
        params = {
            "access_token": getattr(settings, 'GUMROAD_ACCESS_TOKEN'),
            "email": email
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            json_response = response.json()
            sales_data = json_response.get('sales', [])
            sales.extend(x for x in sales_data if x not in sales)
            sales.append({'payment_processor': 'Gumroad'})
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    

    for purchase in Purchase.objects.filter(Q(email=request.user.profile.email) | Q(email=request.user.email)):
        for product in purchase.products.all():
            sales.append({
                'product_name': product.name,
                'created_at': purchase.timestamp,
                'payment_processor': 'Stripe'
            })

    context = {
        'parent': 'download',
        'segment': 'paid_downloads',
        'sales': sales,
        'page_title': 'Dashboard - Paid Products',
    }
    return render(request, 'dashboard/downloads/paid-downloads.html', context)


@login_required(login_url='/users/signin/')
def generated_apps(request):
    apps = GeneratedApp.objects.filter(user=request.user).order_by("-generated_at")[:25]
    context = {
        'parent': 'download',
        'segment': 'generated_apps',
        'apps': apps,
        'page_title': 'Dashboard - Generated Apps',
    }
    return render(request, 'dashboard/downloads/generated-apps.html', context)


@login_required(login_url='/users/signin/')
def delete_generated_app(request, pk):
    app = get_object_or_404(GeneratedApp, pk=pk)
    app.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/signin/')
def download_generated_app(request, pk):
    app = get_object_or_404(GeneratedApp, pk=pk)
    base_dir = settings.BASE_DIR
    generated_apps_dir = os.path.join(base_dir, 'generated_code')
    file_path = os.path.join(generated_apps_dir, f"{app.task_id}.zip")

    if not os.path.exists(file_path):
        raise Http404(f"File not found: {file_path}")

    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="{app.task_id}.zip"'
    return response

#

def user_filter(request):
    filter_string = {}
    filter_mappings = {
        'search': 'username__icontains'
    }
    for key in request.GET:
        if request.GET.get(key) and key != 'page':
            filter_string[filter_mappings[key]] = request.GET.get(key)

    return filter_string


@staff_member_required(login_url='/admin/')
def user_list(request):
    filters = {}
    if search := request.GET.get('search'):
        if re.match(r"[^@]+@[^@]+\.[^@]+", search):
            filters['email__icontains'] = search
        else:
            filters['username__icontains'] = search

    user_list = User.objects.filter(**filters)

    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 25)
    users = paginator.page(page)

    context = {
        'users': users,
        'segment': 'users',
        'page_title': 'Dashboard - All Users',
    }
    return render(request, 'pages/users.html', context)


@staff_member_required(login_url='/admin/')
def make_user_pro(request, username):
    profile = Profile.objects.get(user__username=username)
    profile.pro = True
    profile.save()

    return redirect(request.META.get('HTTP_REFERER'))


@staff_member_required(login_url='/admin/')
def send_email_to_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(
            subject,
            message,
            getattr(settings, 'EMAIL_HOST_USER'),
            [user.email],
            fail_silently=False,
        )

    return redirect(request.META.get('HTTP_REFERER'))



# File Manager

def convert_csv_to_text(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    text = ''
    for row in rows:
        text += ','.join(row) + '\n'

    return text


def get_files_from_directory(directory_path):
    files = []
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            try:
                print( ' > file_path ' + file_path)
                _, extension = os.path.splitext(filename)
                if extension.lower() == '.csv':
                    csv_text = convert_csv_to_text(file_path)
                else:
                    csv_text = ''

                files.append({
                    'file': file_path.split(os.sep + 'media' + os.sep)[1],
                    'filename': filename,
                    'file_path': file_path,
                    'csv_text': csv_text
                })
            except Exception as e:
                print( ' > ' +  str( e ) )   

    return files


@login_required(login_url='/accounts/login-v1/')
def save_info(request, file_path):
    path = file_path.replace('%slash%', '/')
    if request.method == 'POST':
        FileInfo.objects.update_or_create(
        path=path,
        defaults={
            'info': request.POST.get('info')
        }
    )
    
    return redirect(request.META.get('HTTP_REFERER'))

def get_breadcrumbs(request):
    path_components = [component for component in request.path.split("/") if component]
    breadcrumbs = []
    url = ''

    for component in path_components:
        url += f'/{component}'

        if component == "dashboard":
            continue

        if component == "file-manager":
            component = "media"

        breadcrumbs.append({'name': component, 'url': url})

    return breadcrumbs

@login_required(login_url='/accounts/login-v1/')
def file_manager(request, directory=''):
    user_id = str(request.user.id)
    media_path = os.path.join(settings.MEDIA_ROOT, user_id, 'files')

    if not os.path.exists(media_path):
        os.makedirs(media_path)
        
    directories = generate_nested_directory(media_path, media_path)
    selected_directory = directory

    files = []
    selected_directory_path = os.path.join(media_path, selected_directory)
    if os.path.isdir(selected_directory_path):
        files = get_files_from_directory(selected_directory_path)

    breadcrumbs = get_breadcrumbs(request)

    context = {
        'directories': directories, 
        'files': files, 
        'selected_directory': selected_directory,
        'segment': 'file_manager',
        'parent': 'settings',
        'breadcrumbs': breadcrumbs,
        'user_id': str(request.user.id),
    }
    return render(request, 'dashboard/file-manager.html', context)


def generate_nested_directory(root_path, current_path):
    directories = []
    for name in os.listdir(current_path):
        if os.path.isdir(os.path.join(current_path, name)):
            unique_id = str(uuid.uuid4())
            nested_path = os.path.join(current_path, name)
            nested_directories = generate_nested_directory(root_path, nested_path)
            directories.append({'id': unique_id, 'name': name, 'path': os.path.relpath(nested_path, root_path), 'directories': nested_directories})
    return directories


@login_required(login_url='/accounts/login-v1/')
def delete_file(request, file_path):
    path = file_path.replace('%slash%', '/')
    absolute_file_path = os.path.join(settings.MEDIA_ROOT, path)
    os.remove(absolute_file_path)
    print("File deleted", absolute_file_path)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/accounts/login-v1/')
def download_file(request, file_path):
    path = file_path.replace('%slash%', '/')
    absolute_file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(absolute_file_path):
        with open(absolute_file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(absolute_file_path)
            return response
    raise Http404(f"/download-file/{file_path}")

@login_required(login_url='/accounts/login-v1/')
def upload_file(request):
    media_path = os.path.join(settings.MEDIA_ROOT)
    user_subdirectory = str(request.user.id)
    media_user_path = os.path.join(media_path, user_subdirectory, 'files')

    # Create the user-specific subdirectory if it doesn't exist
    if not os.path.exists(media_user_path):
        os.makedirs(media_user_path)

    selected_directory = request.POST.get('directory', '')
    selected_directory_path = os.path.join(media_user_path, selected_directory)

    if request.method == 'POST':
        
        total_files = 0
        for root, dirs, files in os.walk(media_user_path):
            total_files += len([file for file in files if os.path.isfile(os.path.join(root, file))])
        
        max_files = 5
        if total_files >= max_files:
            messages.error(request, f"File limit of {max_files} files reached in this directory.")
            return redirect(request.META.get('HTTP_REFERER'))

        file = request.FILES.get('file')
        max_size_kb = 50
        if file.size > max_size_kb * 1024:
            messages.error(request, f'File size exceeds the limit of {max_size_kb}KB.')
            return redirect(request.META.get('HTTP_REFERER'))
        
        file_path = os.path.join(selected_directory_path, file.name)

        with open(file_path, 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

    return redirect(request.META.get('HTTP_REFERER'))


from django.http import JsonResponse

def auth_status(request):
    #return JsonResponse({"logged_in": request.user.is_authenticated})
    return JsonResponse({"logged_in": True})

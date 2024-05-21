import base64
import datetime
import json

from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.core.paginator import Paginator
from apps.blog.forms import ArticleForm
from apps.common.models import State, Tag, Article, Bookmark

def blogs(request):
    page = request.GET.get('page', 1)
    search_query = request.GET.get('search', '')
    
    articles = Article.objects.filter(title__icontains=search_query, state=State.PUBLISHED).order_by('-published_at')
    paginator = Paginator(articles, per_page=12)

    context = {
        'articles': paginator.get_page(page),
        'total_pages': paginator.num_pages,
        'segment': 'blog'
    }

    return render(request, 'pages/blogs/index.html', context)

def blog_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    tag_ids = article.tags.values_list('id', flat=True)
    articles = Article.objects.filter(state=State.PUBLISHED, tags__in=tag_ids).exclude(id=article.id).order_by('?')[:4]
    tags = article.tags.all()
    is_bookmarked = request.user.is_authenticated and Bookmark.objects.filter(article=article, user=request.user).exists()
    
    context = {
        'article': article,
        'articles': articles,
        'tags': tags,
        'segment': 'blog',
        'is_bookmarked': is_bookmarked
    }
    
    return render(request, 'pages/blogs/blog-detail.html', context)

def filter_by_tags(request, slug):
    page = request.GET.get('page', 1)
    tag = get_object_or_404(Tag, slug=slug)
    articles = Article.objects.filter(state=State.PUBLISHED, tags=tag)
    paginator = Paginator(articles, per_page=12)

    context = {
        'articles': paginator.get_page(page),
        'total_pages': paginator.num_pages,
        'segment': 'blog'
    }
    return render(request, 'pages/blogs/filter-by-tags.html', context)


def add_bookmark(request, slug):
    article = get_object_or_404(Article, slug=slug)
    bookmark = Bookmark.objects.filter(article=article, user=request.user)
    if bookmark.exists():
        bookmark.delete()
    else:
        Bookmark.objects.create(article=article, user=request.user)

    return redirect(request.META.get('HTTP_REFERER'))


def create_blog(request):
    form = ArticleForm()
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            article = Article.objects.create(
                title=data.get('title'),
                subtitle=data.get('subtitle'),
                content=data.get('content'),
                thumbnail=data.get('thumbnail'),
                created_by=request.user
            )

            if 'draft' in request.POST:
                article.state = State.DRAFT
            else:
                article.state = State.PUBLISHED
                article.published_at = datetime.datetime.now()

            article.tags.set(data.get('tags'))
            article.save()

            return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form
    }
    return render(request, 'pages/blogs/create-blog.html', context)
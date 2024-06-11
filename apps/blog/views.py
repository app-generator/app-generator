from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from apps.common.models import State, Tag, Article, Bookmark, VisibilityChoices

def blogs(request, tags=None):
    page = request.GET.get('page', 1)
    search_query = request.GET.get('search', '')
    
    articles = Article.objects.filter(title__icontains=search_query, state=State.PUBLISHED, visibility=VisibilityChoices.PUBLIC)
    if request.user.is_authenticated:
        if request.user.profile.pro:
            articles = articles | Article.objects.filter(title__icontains=search_query, state=State.PUBLISHED, visibility=VisibilityChoices.PRO_USER)
        else:
            articles = articles | Article.objects.filter(title__icontains=search_query, state=State.PUBLISHED, visibility=VisibilityChoices.AUTHENTICATED_USER)
    
    tag_list = []
    if tags:
        tag_list = tags.split(',')
        articles = articles.filter(tags__slug__in=tag_list).distinct()
    
    articles = articles.order_by('-published_at')
    paginator = Paginator(articles, per_page=12)
    tags = Tag.objects.all()

    context = {
        'articles': paginator.get_page(page),
        'total_pages': paginator.num_pages,
        'segment': 'blog',
        'tags': tags,
        'tag_list': tag_list
    }

    return render(request, 'pages/blogs/index.html', context)

def blog_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    tag_ids = article.tags.values_list('id', flat=True)

    if article.visibility != VisibilityChoices.PUBLIC:
        if not request.user.is_authenticated:
            return redirect('signin')

    articles = Article.objects.filter(state=State.PUBLISHED, visibility=VisibilityChoices.PUBLIC, tags__in=tag_ids).exclude(id=article.id).order_by('?')[:4]
    if request.user.is_authenticated:
        
        if request.user.profile.pro:
            articles = articles | Article.objects.filter(state=State.PUBLISHED, visibility=VisibilityChoices.PRO_USER, tags__in=tag_ids).exclude(id=article.id).order_by('?')[:4]
        else:
            articles = articles | Article.objects.filter(state=State.PUBLISHED, visibility=VisibilityChoices.AUTHENTICATED_USER, tags__in=tag_ids).exclude(id=article.id).order_by('?')[:4]
    

    tags = article.tags.all()
    is_bookmarked = request.user.is_authenticated and Bookmark.objects.filter(article=article, user=request.user).exists()

    context = {
        'article': article,
        'articles': articles,
        'tags': tags,
        'segment': 'blog',
        'is_bookmarked': is_bookmarked,

        'page_title' : article.title,
        'page_info' : article.subtitle,
        'page_keywords' : ', '.join([tag.name for tag in article.tags.all()])
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


@login_required(login_url='/users/signin/')
def add_bookmark(request, slug):
    article = get_object_or_404(Article, slug=slug)
    bookmark = Bookmark.objects.filter(article=article, user=request.user)
    if bookmark.exists():
        bookmark.delete()
    else:
        Bookmark.objects.create(article=article, user=request.user)

    return redirect(request.META.get('HTTP_REFERER'))
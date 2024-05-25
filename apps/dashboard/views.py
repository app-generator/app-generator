from django.shortcuts import render, redirect
from apps.common.models_blog import Article, Bookmark
from django.contrib.auth.decorators import login_required
from apps.blog.forms import ArticleForm

# Create your views here.

@login_required(login_url='/users/login/')
def blog_dashboard(request):
    filter_string = {}
    if search := request.GET.get('search'):
        filter_string['title__icontains'] = search

    articles = Article.objects.filter(created_by=request.user, **filter_string).order_by('-published_at')

    context = {
        'segment': 'blog_dashboard',
        'parent': 'blog',
        'articles': articles,
    }
    return render(request, 'dashboard/blog/index.html', context)


@login_required(login_url='/users/login/')
def bookmarked_blog(request):
    filter_string = {}
    if search := request.GET.get('search'):
        filter_string['article__title__icontains'] = search

    bookmarked_articles = Bookmark.objects.filter(user=request.user, **filter_string)

    context = {
        'segment': 'bookmarked_blog',
        'parent': 'blog',
        'bookmarked_articles': bookmarked_articles
    }
    return render(request, 'dashboard/blog/bookmarked-blog.html', context)

@login_required(login_url='/users/login/')
def delete_blog(request, slug):
    article = Article.objects.get(slug=slug)
    article.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def update_blog(request, slug):
    article = Article.objects.get(slug=slug)
    initial_data = {
        'title': article.title,
        'content': article.content,
        'subtitle': article.subtitle,
        'tags': article.tags.all(),
        'thumbnail': article.thumbnail,
    }
    form = ArticleForm(initial=initial_data)

    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.subtitle = request.POST.get('subtitle')
        article.content = request.POST.get('content')

        if request.FILES.get('thumbnail'):
            article.thumbnail = request.FILES.get('thumbnail')

        article.tags.set(request.POST.getlist('tags'))

        article.save()
        return redirect(request.META.get('HTTP_REFERER'))
    
    context = {
        'article': article,
        'form': form,
        'segment': 'blog_dashboard',
        'parent': 'blog',
    }
    return render(request, 'dashboard/blog/update-blog.html', context)
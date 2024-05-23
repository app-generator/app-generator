from django.shortcuts import render, redirect
from apps.common.models_blog import Article
from django.contrib.auth.decorators import login_required
from apps.blog.forms import ArticleForm

# Create your views here.

@login_required(login_url='/users/login/')
def blog_dashboard(request):
    filter_string = {}
    if search := request.GET.get('search'):
        filter_string['title__icontains'] = search

    articles = Article.objects.filter(created_by=request.user, **filter_string).order_by('-published_at')
    form = ArticleForm()

    context = {
        'segment': 'blog_dashboard',
        'articles': articles,
        'form': form
    }
    return render(request, 'dashboard/blog/index.html', context)


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
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            article.title = data.get('title')
            article.subtitle = data.get('subtitle')
            article.content = data.get('content')

            if data.get('thumbnail'):
                article.thumbnail = data.get('thumbnail')

            article.save()

            return redirect(request.META.get('HTTP_REFERER'))
    
    context = {
        'article': article,
        'form': form,
        'segment': 'blog_dashboard',
    }
    return render(request, 'dashboard/blog/update-blog.html', context)
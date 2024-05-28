import datetime
from django.shortcuts import render, redirect
from apps.common.models_blog import Article, Bookmark, File, FileType, State, Tag
from django.contrib.auth.decorators import login_required
from apps.blog.forms import ArticleForm
from django.urls import reverse
from django.contrib import messages
from apps.common.models_products import Products
from apps.products.forms import ProductForm
from django.utils.text import slugify

# Create your views here.


# Blog article
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
    messages.success(request, 'Blog deleted successfully!')
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/signin/')
def create_blog(request):
    form = ArticleForm()
    tags = Tag.objects.all()
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            article = Article.objects.create(
                title=data.get('title'),
                subtitle=data.get('subtitle'),
                content=data.get('content'),
                created_by=request.user
            )

            if thumbnail := data.get('thumbnail'):
                article.thumbnail = File.objects.create(file=thumbnail, created_by=request.user, type=FileType.IMAGE)
            
            if video := data.get('video'):
                article.video = File.objects.create(url=video, created_by=request.user, type=FileType.VIDEO)

            if request.user.profile.is_trusted_editor:
                article.state = State.PUBLISHED
                article.published_at = datetime.datetime.now()
            else:
                article.state = State.DRAFT

            article.tags.set(data.get('tags'))
            article.save()
            messages.success(request, 'Blog created successfully!')

            return redirect(reverse('update_blog', args=[article.slug]))

    context = {
        'form': form,
        'segment': 'create_article',
        'parent': 'blog',
        'tags': [{'name': tag.name, 'slug': tag.slug} for tag in tags]
    }
    return render(request, 'dashboard/blog/create-blog.html', context)

@login_required(login_url='/users/login/')
def update_blog(request, slug):
    article = Article.objects.get(slug=slug)
    initial_data = {
        'title': article.title,
        'content': article.content,
        'subtitle': article.subtitle,
        'tags': article.tags.all(),
        'thumbnail': article.thumbnail,
        'video': article.video.url if article.video else None,
    }
    form = ArticleForm(initial=initial_data)

    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.subtitle = request.POST.get('subtitle')
        article.content = request.POST.get('content')

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
    }
    return render(request, 'dashboard/blog/update-blog.html', context)


# Product

@login_required(login_url='/users/login/')
def product_dashboard(request):
    filter_string = {}
    if search := request.GET.get('search'):
        filter_string['name__icontains'] = search

    products = Products.objects.filter(**filter_string)

    context = {
        'products': products,
        'parent': 'products',
        'segment': 'product_dashboard',
    }
    return render(request, 'dashboard/product/index.html', context)

@login_required(login_url='/users/login/')
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
    }
    return render(request, 'dashboard/product/create.html', context)


@login_required(login_url='/users/login/')
def update_product(request, slug):
    product = Products.objects.get(slug=slug)
    form = ProductForm(instance=product, remove_slug=True)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product, remove_slug=True)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
        'product': product,
        'parent': 'products',
        'segment': 'product_dashboard',
    }
    return render(request, 'dashboard/product/update.html', context)


@login_required(login_url='/users/login/')
def delete_product(request, slug):
    product = Products.objects.get(slug=slug)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect(request.META.get('HTTP_REFERER'))
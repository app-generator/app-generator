import base64, requests
from django.shortcuts import render, redirect, get_object_or_404
from apps.common.models import Products, Type, Tech1, Tech2, CssSystem, DesignSystem, Download
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse, HttpResponseNotFound, Http404 
from django.utils.safestring import mark_safe
from django.db.models import Count
import markdown2

# Create your views here.

def get_filtered_choices(choices):
    return [{'value': choice[0], 'label': choice[1]} for choice in choices if choice[0] != 'NA']

def get_values(choices):
    return [choice[0] for choice in choices if choice[0]!= 'NA']

def products_view(request, tags=None):
    filter_string = {}
    if search := request.GET.get('search'):
        filter_string['name__icontains'] = search

    products = Products.objects.filter(**filter_string)

    tag_list = []
    if tags:
        tag_list = tags.split(',')
    
    tag_filters = Q()
    for tag in tag_list:
        if tag in get_values(Tech1.choices):
            tag_filters |= Q(tech1=tag)
        elif tag in get_values(Tech2.choices):
            tag_filters |= Q(tech2=tag)
        elif tag in get_values(CssSystem.choices):
            tag_filters |= Q(design_css=tag)
        elif tag in get_values(DesignSystem.choices):
            tag_filters |= Q(design_system=tag)

    products = products.filter(tag_filters)

    if request.GET.get('free') == 'True':
        products = products.filter(free=True)
    
    if sort := request.GET.get('sort'):
        if sort == 'most-downloaded':
            products = products.annotate(download_count=Count('download')).order_by('-download_count')

    combined_choices = {
        'tech1': get_filtered_choices(Tech1.choices),
        'tech2': get_filtered_choices(Tech2.choices),
        'css_system': get_filtered_choices(CssSystem.choices),
        'design_system': get_filtered_choices(DesignSystem.choices),
    }

    context = {
        'page_title': 'Free and PAID starters but with Djang0, Flask, Node, and React',
        'page_info': 'Production-ready starters crafted by AppSeed.',
        'page_keywords': 'django, starters, flask, node, react',
        'combined_choices': combined_choices,
        'tag_list': tag_list,
        'products': products
    }
    return render(request, 'pages/products/index.html', context)

def products_design(request, design):

    free_products = Products.objects.filter(design=design).filter(free=True)
    paid_products = Products.objects.filter(design=design).filter(free=False)

    design_label = design.replace('-', ' ').title()

    context = {
        'page_title': f"{design_label} Starters - built with Django, Flask, Node, and React",
        'page_info': f"Production-ready starters crafted by App-Generator on top of {design_label} design",
        'page_keywords': 'django, starters, flask, node, react' + design,
        'free_products': free_products,
        'paid_products': paid_products,
        'design': design,
        'design_label': design_label
    }
    return render(request, 'pages/products/by_design.html', context)

def products_by_tech1(request, design, tech1):
    filter_string = {}
    if search := request.GET.get('search'):
        filter_string['name__icontains'] = search

    free_products = Products.objects.filter(design_system=design, tech1=tech1, **filter_string).filter(free=True)[:3]
    paid_products = Products.objects.filter(design_system=design, tech1=tech1, **filter_string).filter(free=False)[:3]

    context = {
        'free_products': free_products,
        'paid_products': paid_products    }
    return render(request, 'pages/products/tech1-products.html', context)

def product_detail(request, design, tech1):

    product = get_object_or_404(Products, design=design, tech1=tech1)

    context = {
        'product': product,
        'page_title': product.seo_title,
        'page_info': product.seo_description,
        'page_keywords': product.seo_tags,
        'page_canonical': product.canonical
    }

    if product.free:
        return render(request, 'pages/products/free-product-detail.html', context)
    else:
        return render(request, 'pages/products/pro-product-detail.html', context)

def product_detail_fullstack(request, design, tech1, tech2):

    product = get_object_or_404(Products, design=design, tech1=tech1, tech2=tech2)

    context = {
        'product': product,
        'page_title': product.seo_title,
        'page_info': product.seo_description,
        'page_keywords': product.seo_tags,
        'page_canonical': product.canonical
    }

    if product.free:
        return render(request, 'pages/products/free-product-detail.html', context)
    else:
        return render(request, 'pages/products/pro-product-detail.html', context)
    
@login_required(login_url='/users/signin/')
def download_product(request, slug):
    product = get_object_or_404(Products, slug=slug)
    if request.method == 'POST':
        dw_url = request.POST.get('dw_url')
        if dw_url and dw_url.endswith(".zip"):
            download = Download.objects.create(product=product, user=request.user)
            product.downloads += 1
            download.downloaded_at = timezone.now()
            download.save()

            return redirect(dw_url)
        

    return redirect(request.META.get('HTTP_REFERER'))


def fetch_changelog_content(url):
    if not url:
        return HttpResponse('<p>Invalid URL.</p>', content_type='text/html')
    
    parts = url.split('/')
    if len(parts) < 5 or parts[2] != 'github.com':
        return HttpResponse('<p>Invalid GitHub URL.</p>', content_type='text/html')
    
    username = parts[3]
    repository = parts[4]
    
    api_url = f'https://api.github.com/repos/{username}/{repository}/contents/CHANGELOG.md'

    response = requests.get(api_url)
    
    if response.status_code == 200:
        file_content = response.json()['content']
        markdown_content = base64.b64decode(file_content).decode('utf-8')
        
        html_rendered = markdown2.markdown(markdown_content)
    else:
        html_rendered = '<p>Unable to fetch changelog at this time.</p>'
    
    return mark_safe(html_rendered)


def fetch_changelog_view(request):
    url = request.GET.get('url')
    html_rendered = fetch_changelog_content(url)
    return HttpResponse(html_rendered, content_type='text/html')

# Categories

'''
type=Type.WEBAPP, DASHBOARD, API
tech=Tech1 or Tech2
filter_string=free, paid, all, most_downloaded
'''

def get_products(product_type, request, aTech=None, aType=None):

    type_mapping = {
        'free': True,
        'open-source': True
    }

    filter_string = {'type': product_type}
    if search := request.GET.get('search'):
        filter_string['name__icontains'] = search

    if request.GET.get('free') == 'True':
        filter_string['free'] = True

    if aTech:
        if aTech == 'free' or aTech == 'open-source':
            filter_string['free'] = True
        elif aTech == 'paid':
            filter_string['free'] = False
        else:
            filter_string['tech1'] = aTech

    if aType:
        filter_string['free'] = type_mapping.get(aType, False)

    products = Products.objects.filter(**filter_string)

    if sort := request.GET.get('sort'):
        if sort == 'most-downloaded':
            products = products.annotate(download_count=Count('download')).order_by('-download_count')

    grouped_products = {}

    for product in products:
        tech1 = product.tech1
        grouped_products.setdefault(tech1, []).append(product)

    return grouped_products

def dashboards(request, aTech=None, aType=None):

    if aType:
        aType = aType.lower()

        if aType not in ['free', 'paid']:
            raise Http404(request.path)

    grouped_products = get_products(Type.DASHBOARD, request, aTech, aType)
    categs_l = list( grouped_products.keys() )
    categs   = ', '.join( categs_l ) 

    nbr_products = 0
    for c in grouped_products.keys():
        nbr_products += len( grouped_products [c] )

    context = {
        'segment':'/admin-dashboards/',
        'grouped_products' : grouped_products
    }

    context['page_canonical'] = request.path

    if aTech:
        context['page_title'] = aTech.title() + ' Admin Dashboards' 
    else:
        context['page_title'] = ' Admin Dashboards'

    context['content_title'] = context['page_title'] 
    context['page_info'] = 'Index with production-ready ' + context['page_title'] + ' with best practices applied, authentication, modern UI, docker and common modules'
    context['content_info'] = context['page_info'] 

    if 'free' == aType:        
        context['page_title'] += f" - {nbr_products} {categs} open-source starters"
    elif 'paid' == aType:
        context['page_title'] += f" - {nbr_products} {categs} paid (premium) starters"
    else:
        context['page_title'] += f" - {nbr_products} {categs} open-source and paid (premium) starters"
    
    context['page_keywords'] = f"dashboards, admin dashboards, admin panels, full-stack dashboards, full-stack admin panels, {categs} dashboards, {categs} admin panels"
    
    context['page_keywords'] += f", {categs} dashboards"

    return render(request, 'pages/category/index.html', context)

def apps(request, aTech=None, aType=None):

    if aType:
        aType = aType.lower()

        if aType not in ['free', 'paid']:
            raise Http404(request.path)

    grouped_products = get_products(Type.WEBAPP, request, aTech, aType)
    categs_l = list( grouped_products.keys() )
    categs   = ', '.join( categs_l ) 

    nbr_products = 0
    for c in grouped_products.keys():
        nbr_products += len( grouped_products [c] )

    context = {
        'segment':'/apps/',
        'grouped_products' : grouped_products
    }

    context['page_canonical'] = request.path

    if aTech:
        context['page_title'] = aTech.title() + ' Web Apps' 
    else:
        context['page_title'] = ' Web Apps'

    context['content_title'] = context['page_title'] 
    context['page_info'] = 'Index with production-ready ' + context['page_title'] + ' with best practices applied, authentication, modern UI, docker and common modules'
    context['content_info'] = context['page_info'] 

    if 'free' == aType:        
        context['page_title'] += f" - {nbr_products} {categs} open-source starters"
    elif 'paid' == aType:
        context['page_title'] += f" - {nbr_products} {categs} paid (premium) starters"
    else:
        context['page_title'] += f" - {nbr_products} {categs} open-source and paid (premium) starters"
    
    context['page_keywords'] = f"apps, web apps, ecommerce, presentation starters, full-stack web apps, {categs} web apps, {categs} app templates"
    
    context['page_keywords'] += f", {categs} apps"

    return render(request, 'pages/category/index.html', context)


def ui_kit(request, design_system=None):

    context = {}

    filter_string = {}
    if search := request.GET.get('search'):
        filter_string['name__icontains'] = search

    if request.GET.get('free') == 'True':
        filter_string['free'] = True

    if design_system:
        filter_string['design_system'] = design_system
    
    products = Products.objects.filter(**filter_string)

    if sort := request.GET.get('sort'):
        if sort == 'most-downloaded':
            products = products.annotate(download_count=Count('download')).order_by('-download_count')

    grouped_products = {}

    for product in products:
        design_system = product.design_system
        grouped_products.setdefault(design_system, []).append(product)

    context['grouped_products'] = grouped_products

    grouped_keys_l = list( grouped_products.keys() )
    grouped_keys_l = [item.title() for item in grouped_keys_l]
    grouped_keys = ', '.join( grouped_keys_l )
    context['page_title'] = f"{grouped_keys} - Production-ready starters for Django, Flask, React built on well-known kits like {grouped_keys}"

    return render(request, 'pages/category/index.html', context)


def agency(request, design_by=None):
    
    context = {}
    filter_string = {}
    
    if search := request.GET.get('search'):
        filter_string['name__icontains'] = search

    if request.GET.get('free') == 'True':
        filter_string['free'] = True

    company_link = True
    company_name = None

    if design_by:
        company_name = design_by
        company_link = False
        filter_string['design_by'] = design_by
    else:
        pass 
    
    products = Products.objects.filter(**filter_string)

    if sort := request.GET.get('sort'):
        if sort == 'most-downloaded':
            products = products.annotate(download_count=Count('download')).order_by('-download_count')

    grouped_products = {}

    for product in products:
        design_by = product.design_by
        grouped_products.setdefault(design_by, []).append(product)

    context['grouped_products'] = grouped_products
    context['company_link'] = company_link

    grouped_keys_l = list( grouped_products.keys() )
    grouped_keys_l = [item.title() for item in grouped_keys_l]
    grouped_keys = ', '.join( grouped_keys_l )
    context['page_title'] = f"{grouped_keys} - Production-ready starters for Django, Flask, React built on well-known kits designed by {grouped_keys}"

    return render(request, 'pages/category/index.html', context)

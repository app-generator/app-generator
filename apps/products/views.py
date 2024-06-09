from django.shortcuts import render
from apps.common.models_products import Products, Type, Tech1, Tech2, CssSystem, DesignSystem
from django.db.models import Count
from django.db.models import QuerySet
from django.db.models import Q

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
    grouped_products = {}

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
    
    for product in products:
        tech1 = product.tech1

        if tech1 not in grouped_products:
            grouped_products[tech1] = []

        grouped_products[tech1].append(product)

    combined_choices = {
        'tech1': get_filtered_choices(Tech1.choices),
        'tech2': get_filtered_choices(Tech2.choices),
        'css_system': get_filtered_choices(CssSystem.choices),
        'design_system': get_filtered_choices(DesignSystem.choices),
    }

    context = {
        'grouped_products': grouped_products,
        'page_title': 'Free and PAID starters but with Djang0, Flask, Node, and React',
        'page_info': 'Production-ready starters crafted by AppSeed.',
        'page_keywords': 'django, starters, flask, node, react',
        'combined_choices': combined_choices,
        'tag_list': tag_list
    }
    return render(request, 'pages/products/index.html', context)


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



# Admin dashboard

def admin_dashboard(request):
    filter_string = {}
    if search := request.GET.get('search'):
        filter_string['name__icontains'] = search

    products = Products.objects.filter(type=Type.DASHBOARD, **filter_string)
    grouped_products = {}

    for product in products:
        tech1 = product.tech1

        if tech1 not in grouped_products:
            grouped_products[tech1] = []

        grouped_products[tech1].append(product)

    context = {
        'grouped_products': grouped_products
    }
    return render(request, 'pages/admin-dashboard/index.html', context)

def admin_dashboard_by_tech1(request, tech1):
    filter_string = {}
    if search := request.GET.get('search'):
        filter_string['name__icontains'] = search

    products = Products.objects.filter(type=Type.DASHBOARD, tech1=tech1, **filter_string)

    context = {
        'products': products
    }
    return render(request, 'pages/admin-dashboard/tech1-products.html', context)


def product_detail(request, design, tech1):
    product = Products.objects.get(design=design, tech1=tech1)

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
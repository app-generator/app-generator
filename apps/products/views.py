from django.shortcuts import render
from apps.common.models_products import Products, Type
from django.db.models import Count
from django.db.models import QuerySet

# Create your views here.


def products_view(request):
    filter_string = {}
    if search := request.GET.get('search'):
        filter_string['name__icontains'] = search

    products = Products.objects.filter(**filter_string)
    grouped_products = {}

    for product in products:
        tech1 = product.tech1
        tech2 = product.tech2

        if tech1 not in grouped_products:
            grouped_products[tech1] = {}

        if tech2 not in grouped_products[tech1]:
            grouped_products[tech1][tech2] = []

        grouped_products[tech1][tech2].append(product)

    context = {
        'grouped_products': grouped_products
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
        'paid_products': paid_products
    }
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

    print(grouped_products)

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
        'product': product
    }
    if product.free:
        return render(request, 'pages/products/free-product-detail.html', context)
    else:
        return render(request, 'pages/products/pro-product-detail.html', context)
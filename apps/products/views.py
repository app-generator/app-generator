from django.shortcuts import render
from apps.common.models_products import Products
from django.db.models import Count
from django.db.models import QuerySet

# Create your views here.


def products_view(request):
    products = Products.objects.all()
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


def products_by_tech1(request, tech1):
    free_products = Products.objects.filter(tech1=tech1).filter(free=True)[:3]
    paid_products = Products.objects.filter(tech1=tech1).filter(free=False)[:3]

    context = {
        'free_products': free_products,
        'paid_products': paid_products
    }
    return render(request, 'pages/products/tech1-products.html', context)
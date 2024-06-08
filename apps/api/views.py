from rest_framework import generics
from apps.api.serializers import ProductSerializer
from apps.common.models import Products, Tech1, Type
from django_filters.rest_framework import DjangoFilterBackend

import django_filters


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Products
        fields = {
            'tech1': ['exact'],
            'tech2': ['exact'],
            'design_by': ['exact'],
            'design_system': ['exact'],
            'design_css': ['exact'],
        }


class ProductListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class ProductDashboardListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        return Products.objects.filter(type=Type.DASHBOARD)


class ProductAppsListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        return Products.objects.filter(type=Type.WEBAPP)


class ProductAPIListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        return Products.objects.filter(type=Type.API)


class ProductDjangoListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        return Products.objects.filter(tech1=Tech1.DJANGO)


class ProductFlaskListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        return Products.objects.filter(tech1=Tech1.FLASK)


class ProductNodejsListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        return Products.objects.filter(tech1=Tech1.NODEJS)
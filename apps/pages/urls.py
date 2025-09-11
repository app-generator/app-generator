from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product-dashboard/", views.show_dashboard, name="show_dashboard"),
    path("discounts/", views.discounts, name="discounts"),
    path("discounts", views.discounts, name="discounts"),
    path("support/", views.support, name="support"),
    path("services/", views.services, name="services"),
    path("services/custom-development/", views.custom_development, name="custom_development"),
    path("terms/", views.terms, name="terms"),
    path("about/", views.about, name="about"),
    path('onboarding-kit/', views.onboarding, name="onboarding"),
    path("profile/github-<str:username>/", views.user_profile, name="user_profile"),
    path("newsletter/", views.newsletter, name="newsletter"),
    path("create-prompt/", views.create_prompt, name="create_prompt"),
    path("download/app/<str:taskID>", views.download_app, name="download_app"),
    path("download/product/<str:productID>", views.download_product, name="download_product"),

    #
    path('api/get-products/', views.get_products, name='get_products'),
    path('api/product/<int:id>/', views.product_details, name='product_details'),
]

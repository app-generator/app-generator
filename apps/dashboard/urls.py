from django.urls import path
from apps.dashboard import views


urlpatterns = [
    # Blog articles
    path('blogs/', views.blog_dashboard, name="blog_dashboard"),
    path("create-blog/", views.create_blog, name="create_blog"),
    path('update-blog/<str:slug>/', views.update_blog, name="update_blog"),
    path('delete-blog/<str:slug>/', views.delete_blog, name="delete_blog"),
    path('bookmarked-blog/', views.bookmarked_blog, name="bookmarked_blog"),

    # Products
    path('products/', views.product_dashboard, name="product_dashboard"),
    path('create-product/', views.create_product, name="create_product"),
    path('update-product/<str:slug>/', views.update_product, name="update_product"),
    path('delete-product/<str:slug>/', views.delete_product, name="delete_product"),

    # Teams
    path('teams/', views.team_list, name="dashboard_team_list"),
    path('team-detail/<int:team_id>/', views.team_detail, name="dashboard_team_detail"),
    path('team-update/<int:team_id>/', views.edit_team, name="dashboard_edit_team"),
    path('team-delete/<int:team_id>/', views.delete_team, name="dashboard_delete_team"),
    path('remove-member/<int:team_id>/<int:profile_id>/', views.remove_team_member, name="remove_team_member"),

    # Projects
    path('projects/', views.project_list, name="dashboard_project_list"),
    path('project-update/<int:project_id>/', views.edit_project, name="dashboard_edit_project"),
    path('project-delete/<int:project_id>/', views.delete_project, name="dashboard_delete_project"),
]

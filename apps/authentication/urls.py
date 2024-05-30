from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('signin/', views.SignInView.as_view(), name="signin"),
    #path('signup/', views.SignUpView.as_view(), name="signup"),
    path('signout/', views.signout_view, name="signout"),
    # path('password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    # path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(
    #     template_name='authentication/password-change-done.html'
    # ), name="password_change_done"),
    path('password-reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('password-reset-confirm/<uidb64>/<token>/',
        views.UserPasswrodResetConfirmView.as_view(), name="password_reset_confirm"
    ),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='authentication/password-reset-done.html'
    ), name='password_reset_done'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='authentication/password-reset-complete.html'
    ), name='password_reset_complete'),

    path('profile/', views.profile, name='profile'),
    path('upload-avatar/', views.upload_avatar, name='upload_avatar'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('toggle-profile-role/', views.toggle_profile_role, name='toggle_profile_role'),
    path('create-team/', views.create_team, name='create_team'),
    path('create-project/', views.create_project, name='create_project'),
    path('invitations/', views.invitation_list, name='invitation_list'),
    path('accept-invitations/<int:id>/', views.accept_invitations, name='accept_invitations'),
    path('deny-invitations/<int:id>/', views.deny_invitations, name='deny_invitations'),
]
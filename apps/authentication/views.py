from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from django.views.generic import CreateView
from apps.common.models import Profile, Team, Project, TeamInvitation
from apps.authentication.forms import SigninForm, SignupForm, UserPasswordChangeForm, UserSetPasswordForm, UserPasswordResetForm, ProfileForm, CreateProejctForm, CreateTeamForm
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib import messages


class SignInView(LoginView):
    form_class = SigninForm
    template_name = "authentication/sign-in.html"

class SignUpView(CreateView):
    form_class = SignupForm
    template_name = "authentication/sign-up.html"
    success_url = "/users/signin/"

class UserPasswordChangeView(PasswordChangeView):
    template_name = 'authentication/password-change.html'
    form_class = UserPasswordChangeForm

class UserPasswordResetView(PasswordResetView):
    template_name = 'authentication/forgot-password.html'
    form_class = UserPasswordResetForm

class UserPasswrodResetConfirmView(PasswordResetConfirmView):
    template_name = 'authentication/reset-password.html'
    form_class = UserSetPasswordForm


def signout_view(request):
    logout(request)
    return redirect(reverse('signin'))


@login_required(login_url='/users/signin/')
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    team_form = CreateTeamForm()
    project_form = CreateProejctForm()
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            profile = form.save()
            profile.programming_languages.set(form.cleaned_data.get('programming_languages', []))
            profile.frameworks.set(form.cleaned_data.get('frameworks', []))
            profile.deployments.set(form.cleaned_data.get('deployments', []))
            profile.no_codes.set(form.cleaned_data.get('no_codes', []))
            messages.success(request, 'Profile updated successfully')
    else:
        form = ProfileForm(instance=profile)
    
    context = {
        'form': form,
        'team_form': team_form,
        'project_form': project_form,
        'segment': 'profile',
        'parent': 'company_profile'
    }
    return render(request, 'dashboard/profile.html', context)


def upload_avatar(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        profile.avatar = request.FILES.get('avatar')
        profile.save()
        messages.success(request, 'Avatar uploaded successfully')
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/users/signin/')
def delete_account(request):
    request.user.delete()
    return redirect(reverse('signin'))

@login_required(login_url='/users/signin/')
def toggle_profile_role(request):
    profile = get_object_or_404(Profile, user=request.user)
    if profile.role == 'User':
        profile.role = 'Company'
    else:
        profile.role = 'User'

    profile.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/users/signin/')
def create_team(request):
    if request.method == 'POST':
        form = CreateTeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.author = Profile.objects.get(user=request.user)
            team.save()
            # team.members.set(form.cleaned_data.get('members'))
            for member in form.cleaned_data.get('members'):
                invite, created = TeamInvitation.objects.update_or_create(
                    member=member,
                    defaults={
                        'team': team
                    }
                )

            return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/signin/')
def create_project(request):
    if request.method == 'POST':
        form = CreateProejctForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = Profile.objects.get(user=request.user)
            project.save()
            project.technologies.set(form.cleaned_data.get('technologies'))
            return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/signin/')
def invitation_list(request):
    invitations = TeamInvitation.objects.filter(member__user__pk=request.user.pk, accepted=False)

    context = {
        'invitations': invitations,
        'segment': 'invitations',
        'parent': 'company_profile'
    }
    return render(request, 'dashboard/teams/invitations.html', context)


@login_required(login_url='/users/signin/')
def accept_invitations(request, id):
    invitation = TeamInvitation.objects.get(pk=id)
    invitation.accepted = True
    invitation.save()

    team = Team.objects.get(pk=invitation.team.pk)
    team.members.add(invitation.member)
    team.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/signin/')
def deny_invitations(request, id):
    invitation = TeamInvitation.objects.get(pk=id)
    invitation.delete()
    return redirect(request.META.get('HTTP_REFERER'))
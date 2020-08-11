from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import User

from django.contrib.admin.views.decorators import staff_member_required, user_passes_test


def register(request):
    if request.user.is_authenticated:
        return redirect('magazine-home')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created You are now able to login.')
            return redirect('login')

    else:
        form = UserRegisterForm()
    context = {
        'title': 'Register',
        'form': form
    }
    return render(request, 'users/register.html',context)


def profile(request, username):
    context = {
        'title': 'Profile',
        'user_data': User.objects.get(username=username)
    }
    return render(request, 'users/profile.html', context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile', username=request.user.username)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Edit profile'
    }
    return render(request, 'users/update_profile.html', context)

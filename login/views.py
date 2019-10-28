from django.shortcuts import render, HttpResponse, get_object_or_404
from .MyForms import RegistrationForm, LoginForm, ProfileForm, PwdChangeForm
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def profile(request):
    user = User.objects.get(pk=request.user.id)
    userProfile = UserProfile.objects.get(user=user)

    return render(request, 'login/profile.html',{'userProfile':userProfile})


@login_required
def profile_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            user_profile.org = form.cleaned_data['org']
            user_profile.telephone = form.cleaned_data['telephone']
            user_profile.save()

            return HttpResponseRedirect(reverse('profile', args=[user.id]))
    else:
        default_data = {'first_name': user.first_name, 'last_name': user.last_name,
                        'org': user_profile.org, 'telephone': user_profile.telephone, }
        form = ProfileForm(default_data)

    return render(request, 'login/profile_update.html', {'form': form, 'user': user})


def register(request):
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            student_number = form.cleaned_data['student_number']
            email = form.cleaned_data['email']
            group_name = {1:'DS',2:'AZ',3:'YX',4:'WA'}[int(form.cleaned_data['group_name'])]
            # 使用内置User自带create_user方法创建用户，不需要使用save()
            user = User.objects.create_user(username=username, password=password,email=email)

            # 如果直接使用objects.create()方法后不需要使用save()
            user_profile = UserProfile(user=user, student_number=student_number,group_name=group_name)
            user_profile.save()

            return HttpResponseRedirect("/login/")
    else:
        form = RegistrationForm()
    return render(request, 'login/registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/home/")
            else:
                # 登录失败
                return render(request, 'login/login.html',
                              {'form': form, 'message': 'Wrong password Please Try agagin'})
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")


@login_required
def pwd_change(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        form = PwdChangeForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data['old_password']
            username = user.username

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                new_password = form.cleaned_data['password2']
                user.set_password(new_password)
                user.save()
                return HttpResponseRedirect('/accounts/login/')

            else:
                return render(request, 'login/pwd_change.html', {'form': form,
                                                                 'user': user,
                                                                 'message': 'Old password is wrong Try again'})
    else:
        form = PwdChangeForm()

    return render(request, 'login/pwd_change.html', {'form': form, 'user': user})
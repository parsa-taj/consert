from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ticketSales.models import Consert, Favorite


# Create your views here.
def logout_view(request):
    try:
        logout(request)
        return redirect('ticketSales:consert-list')

    except:
        messages.error('something is wrong')

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))

        else:
            return redirect('ticketSales:consert-list')


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # redirect user to page which request to login
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))

            else:
                return redirect('ticketSales:consert-list')
        else:
            messages.error(request, 'username or password is not correct')
            return redirect('account:login')
    else:
        if request.user.is_authenticated:
            return redirect('ticketSales:consert-list')
        return render(request, 'account/login.html')


def sign_up(request):

    if request.method == "POST":
        userForm = UserForm(request.POST, request.FILES)

        if userForm.is_valid():
            userForm.save()
            return redirect('ticketSales:consert-list')

        else:
            messages.error(request, "data is invalid")
            return redirect('account:sign_up')

    else:
        userForm = UserForm()
        context = {
            'userForm': userForm,
        }
        return render(request, 'account/sign_up.html', context=context)


@login_required
def profile(request):
    # if request.method == 'POST':
    #     userForm = UserForm(request.POST, request.FILES, instance=request.user)
    #     # user=User.objects.create_user(username='',email="",password="")
    #     if userForm.is_valid():
    #         userForm.save()

    #         if request.GET.get('next'):
    #             return redirect(request.GET.get('next'))

    #         else:
    #             return redirect('ticketSales:consert-list')

    #     else:
    #         messages.error(request,'data is invalid')
    #         return redirect('account:profile')

    # else:
    #     userForm = UserForm(instance=request.user)

    return render(request, 'account/profile.html')


@login_required
def profileEdit(request):
    if request.method == "POST":
        profileForm = ProfileForm(
            request.POST, request.FILES, instance=request.user)

        if profileForm.is_valid():
            profileForm.save()
            return redirect('account:profile')

        else:
            messages.error(request, 'data is invalid')
            return redirect('account:profile-edit')

    else:
        profileForm = ProfileForm(instance=request.user)
        context = {
            "profileForm": profileForm,
        }
        return render(request, 'account/profile_edit.html', context=context)


@login_required
def showFavorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    singers = []

    for favorite in favorites:
        singers.append(favorite.consert.singer_name) 
        
    context = {
        "favorites": favorites,
        "similar_conserts": Consert.objects.filter(singer_name__in= singers),
    }
    return render(request, 'account/show_favorites.html', context=context)

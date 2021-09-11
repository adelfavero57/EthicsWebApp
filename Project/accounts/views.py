from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

from .forms import CreateUserForm, LoginForm, UpdateUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('managelist')

    # Custom form model imported from forms.py
    form = CreateUserForm()

    # If user has submitted something
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        # Check if all fields are satisfied
        if form.is_valid():
            form.save()
            return redirect(loginPage)

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('managelist')

    # If user has submitted something
    if request.method == "POST":
        form = LoginForm(request.POST)

        # check if all fields are satisfied
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if not remember_me:

                    # will close session after browser is closed
                    request.session.set_expiry(0)
                return redirect('managelist')

        # if user is invalid
        form.custom_error = True
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'login.html', context)


def redirect_view(request):
    return redirect(loginPage)


@login_required(login_url=loginPage)
def editUserPage(request):
    form = UpdateUserForm(instance=request.user)

    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('managelist')

    context = {'form': form}
    return render(request, 'edit_profile.html', context)

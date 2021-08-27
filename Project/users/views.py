from django.shortcuts import render, redirect
from .forms import Register
from django.contrib import messages

# Create your views here.


# Sign up
def index(request):
    if request.method == "POST":
        register_form = Register(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data['username']
            # send data to database
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        register_form = Register()


    return render(request, 'users/index.html', {'form': form})


# Log in

# def login(request):

#     if request.method == "POST":
#         login_form = Register(request.POST)

#         if login_form.is_valid():

#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']

#             if Register.objects.filter(username=username, password=password) != NULL:

#                 messages.success(request, f'successful login for {username}!')

#                 return redirect('Main')

#             else:

#     else:
#         login_form = Register





    
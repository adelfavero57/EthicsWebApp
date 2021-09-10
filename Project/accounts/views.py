from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
from .forms import CreateUserForm

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(loginPage)

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(homePage)

    return render(request, 'login.html')



def homePage(request):
    return render(request, 'home.html')

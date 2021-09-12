from django.contrib.auth import logout
import accounts.views as accounts
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.


class Application:
    def __init__(self, name, username, status):

        self.name = name
        self.process = username
        self.status = status


test1 = Application("form1", "User1", "Checking")
test2 = Application("form2", "User1", "Checking")
test3 = Application("form1", "User2", "Checking")
test4 = Application("form2", "User2", "Checking")
test5 = Application("form3", "User2", "Checking")

Applications = [test1, test2, test3, test4, test5]


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def adminlistPage(request):

    context = {'applications': Applications}
    return render(request, 'adminlist.html', context)

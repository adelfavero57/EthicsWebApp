import accounts.views as accounts
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.


class Application:
    def __init__(self, name, process, status):

        self.name = name
        self.process = process
        self.status = status


test1 = Application("form1", "20%", "IN PROCESS")
test2 = Application("form2", "20%", "IN PROCESS")
test3 = Application("form3", "20%", "IN PROCESS")
test4 = Application("form4", "20%", "IN PROCESS")
test5 = Application("form5", "20%", "IN PROCESS")

Applications = [test1, test2]


@login_required(login_url='login')
def managelistPage(request):

    context = {'applications': Applications}
    return render(request, 'managelist.html', context)

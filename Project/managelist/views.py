from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.shortcuts import render, redirect
from accounts.models import Application
from django.http import JsonResponse

# PDF generation imports
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# Create your views here.

test1 = Application("form1", "20%", "IN PROCESS")
test2 = Application("form2", "20%", "IN PROCESS")
test3 = Application("form3", "20%", "IN PROCESS")
test4 = Application("form4", "20%", "IN PROCESS")
test5 = Application("form5", "20%", "IN PROCESS")

Applications = [test1, test2]

# reportlab documentation for customisation: https://reportlab.com/docs/reportlab-userguide.pdf
def download_application(request):
    #create buffer
    buf = io.BytesIO()
    #create canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    #create text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    
    #content on pdf
    content = [
        "Test line"
        "test line 2"
        "test line 3"
    ]
    for line in content:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='application.pdf')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])
def managelistPage(request):

    applications = Application.objects.filter(user=request.user)
    
    context = {'applications': applications}

    return render(request, 'managelist.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['student'])
# def search(request):
    
#     data = dict()

#     if request.method == "POST":

#         search_text = request.POST["search_text"]

#         if search_text is not None:

#             applications = Application.objects.filter(user=request.user, title=search_text)         

#             data['result'] = applications

            
#     print(data)

#     return JsonResponse(data)
    

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])

def deleteRow(request, item_id):

    item = Application.objects.get(pk=item_id)

    item.delete()

    return redirect('managelist')








from django.shortcuts import render , redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as dj_log
from django.contrib.auth import logout
from datetime import datetime
# from webapp.models import Login
from webapp.models import Contact
from webapp.models import Info

# Create your views here.

def index(request):
    return render(request, 'weby.html')
    

def about(request):
    return render(request, 'about.html' )

def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        con = Contact(name=name, email=email, phone=phone, comment=comment, date=datetime.today())
        con.save()

        messages.success(request, 'Your contact has been sent!')

    return render(request, 'contact.html')
    #return HttpResponse("this is contact django")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            dj_log(request, user )
            # A backend authenticated the credentials
            return redirect('/homelog')
        else:
            messages.error(request, 'Invalid username!')
            # No backend authenticated the credentials
            return render(request, 'login.html')
        
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        user = User.objects.create_user(username , email , pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, 'Your account has been created!')
        return redirect('/login')
    return render(request, 'signup.html')
    


def logout(request):
    logout(request)
    return redirect('/')


def homelog(request):
    return render(request, 'homelog.html')


def info(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        inf = Info(name=name, phone=phone, address=address, date=datetime.today())
        inf.save()

        messages.success(request, 'Your order has been done!')

    return render(request, 'info.html') 
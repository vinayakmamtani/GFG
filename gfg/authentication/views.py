from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from gfg import settings
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    
    if request.method == "POST":
        Name = request.POST('Name')
        regNo = request.POST('Registration Number')
        Pass1 = request.POST('Password')
        Pass2 = request.POST('Confirm Password')
        Hostel_type = request.POST('Hostel Type')
        Hostel_Block = request.POST('Hostel Block')
        roomNo = request.POST('Room Number')
        email = request.POST('Email')
        contactnumber = request.POST('Phone Number')

        if User.objects.filter(regNo=regNo):
            messages.error(request,"Registration Number already exists")
        
        if User.objects.filter(email=email):
            messages.error(request,"Email already exists")
        
        if len(Pass1)<8:
            messages.error(request,"Password too short")
        
        if len(regNo)>9:
            messages.error(request,"Enter a valid Registration Number")
        if len(contactnumber)>10:
            messages.error(request,"Enter a valid Phone Number")
        
        if len(contactnumber)<10:
            messages.error(request,"Enter a valid Phone Number")
        
        if Pass1!=Pass2:    
            messages.error(request,"Passwords do not match")

        if 'gmail.com' in email:
            messages.error(request, "Email from gmail domain is not allowed")

        if 'yahoo.com' in email:
            messages.error(request, "Email from yahoo domain is not allowed")
        
        if 'hotmail.com' in email:
            messages.error(request, "Email from hotmail domain is not allowed")
        
        if 'outlook.com' in email:
            messages.error(request, "Email from outlook domain is not allowed")

        if 'icloud.com' in email:
            messages.error(request, "Email from icloud domain is not allowed")
        
        if 'aol.com' in email:
            messages.error(request, "Email from aol domain is not allowed")
        if 'protonmail.com' in email:
            messages.error(request, "Email from protonmail domain is not allowed")
        
        if not regNo.isalnum():
            messages.error(request, "Registration Number should be alphanumeric")
            return redirect('home')
        
        myuser = User.objects.create_user(Name,email,Pass1,regNo,contactnumber) 
        

        myuser.save() #saves the user

        messages.success(request,"Your account has been successfully created")
        
        
        subject = "Welcome to Bits&Bytes"
        message = "Hello " + myuser.Name + "Welcome to Bits&Bytes Login Page. We are glad to have you here. Hope you have a great time here.\n We are sending you a confirmation email to verify your account \n"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)





        return redirect('signin')
        
def signin(request):
    if request.method == "POST":
        regNo = request.POST('Registration Number')
        Pass1 = request.POST('Password')

        user = authenticate(regNo=regNo,password=Pass1)

        if user is not None:
            login(request,user)
            return render(request, 'authentication/index.html',{"Registration Number":regNo})

        else:
            messages.error(request, "Wrong Credentials!")
            return redirect('home')
def signout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
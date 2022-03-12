from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from django.core.mail import send_mail

# Create your views here.

def load_page(request):
    return render(request,"load_page.html")

def about_page(request):
    return render(request,"about_page.html")

@login_required(login_url='user-login')
@allowed_users(allowed_roles = ['admin', 'staff', 'customer'])
def home_page(request):
    return render(request,"home_page.html")

@login_required(login_url='user-login')
@allowed_users(allowed_roles = ['admin', 'staff'])
def stock_management(request):
    return render(request,"stock_management.html")

@login_required(login_url='user-login')
def mail_sending(request):
    send_mail(
            #SUBJECT
            f'Request from {request.user}',
            #BODY
            f'''
            Email Content
            ''',
            #FROM
            'aflahvk2527@gmail.com',
            #TO
            ['jabeenaj58@gmail.com','rifanasherin22@gmail.com','sneharavindran286@gmail.com'],
            fail_silently=False,
        )
    return render(request,"mail_sending.html")

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def load_page(request):
    return render(request,"loading.html")

def home_page(request):
    return render(request,"home_page.html")

def stock_management(request):
    return render(request,"stock_management.html")

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

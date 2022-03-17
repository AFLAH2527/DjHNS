from itertools import count
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from DjHNS.decorators import allowed_users
from .forms import VaccineRegForm
from .models import VaccineNeedy
from stocks.models import VaccineStock

# Create your views here.

@login_required(login_url='user-login')
@allowed_users(allowed_roles = ['admin', 'staff'])
def vaccine_stock(request):
    vaccine_stock = VaccineStock.objects.all()
    needys = VaccineNeedy.objects.all()
    groups = {}
    for needy in needys :
        if needy.needed_vaccine in groups.keys():
            groups[needy.needed_vaccine] += 1
        else:
            groups[needy.needed_vaccine] = 1

    return render(request,"vaccine/vaccine_stock.html", context={'stock':vaccine_stock, 'groups': groups})

@login_required(login_url='user-login')
def vaccine_about(request):
    return render(request,"vaccine/vaccine_about.html")

@login_required(login_url='user-login')
def vaccine_reg(request):
    form = VaccineRegForm()
    if request.method == "POST":
        form = VaccineRegForm(request.POST)
        if form.is_valid():
            reg_user = form.save()
            current_stock = VaccineStock.objects.get(vaccine_name = reg_user.needed_vaccine)
            if current_stock.count > 0 :
                count = current_stock.count
                # needies = VaccineNeedy.objects.filter(is_mailed=False, needed_vaccine = reg_user.needed_vaccine).order_by('reg_date')
                # for needy in needies:
                #     if count == 0:
                #         break
                print('Mailing ', reg_user.email)
        #         send_mail(
        #     #SUBJECT
        #     f'Vaccine is available',
        #     #BODY
        #     f'''
        #     Email Content
        #     ''',
        #     #FROM
        #     'aflahvk2527@gmail.com',
        #     #TO
        #     [needy.email],
        #     fail_silently=False,
        # )
                reg_user.is_mailed = True 
                reg_user.save()
                count -= 1
                return redirect('home')
            return redirect('home')

    context = {
        "form": form
    }
    return render(request,"vaccine/vaccine_reg.html", context)
 

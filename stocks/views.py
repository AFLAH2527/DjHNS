from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from bloodbank.models import BloodDonor
from stocks.forms import BloodStockCreateForm, VaccineStockCreateForm,BloodStockUpdateForm, VaccineStockUpdateForm
from stocks.models import BloodStock, VaccineStock
from vaccine.models import VaccineNeedy
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url='user-login')
def create_bloodstock(request):
    form = BloodStockCreateForm()
    if request.POST:
        form = BloodStockCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bloodbank/stock')

    return render(request, 'stocks/create_blood.html', context={'form':form})

@login_required(login_url='user-login')
def update_bloodstock(request, id):
    stock = BloodStock.objects.get(id=id)
    old_count = stock.count
    stock.count = 0
    form = BloodStockUpdateForm(instance=stock)
    if request.POST:
        form = BloodStockUpdateForm(request.POST, instance=stock)
        if form.is_valid():
            new_stock = form.save(commit=False)
            new_count = new_stock.count
            new_stock.count += old_count
            if new_stock.count <= new_stock.min_stock:
                                donors = BloodDonor.objects.filter(blood_group=new_stock.blood_group)
                                for donor in donors:
                                    print('Mailing ', donor.email)
                                    send_mail(
                                 #SUBJECT
                                 f'Subject',
                                 #BODY
                                 f'''
                                 Email Content
                                 ''',
                                 #FROM
                                 'aflahvk2527@gmail.com',
                                 #TO
                                 [donor.email],
                                 fail_silently=False,
                             )

            new_stock.save()
            return redirect('/bloodbank/stock')
    return render(request, 'stocks/update_blood.html', context={"form":form})

@login_required(login_url='user-login')
def create_vaccinestock(request):
    form = VaccineStockCreateForm()
    if request.POST:
        form = VaccineStockCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/vaccine/stock')

    return render(request, 'stocks/create_vaccine.html', context={'form':form})

@login_required(login_url='user-login')
def update_vaccinestock(request, id):
    stock = VaccineStock.objects.get(id=id)
    old_count = stock.count
    stock.count = 0
    form = VaccineStockUpdateForm(instance=stock)
    if request.POST:
        form = VaccineStockUpdateForm(request.POST, instance=stock)
        if form.is_valid():
            new_stock = form.save(commit=False)
            new_count = new_stock.count
            count = new_count
            needies = VaccineNeedy.objects.filter(is_mailed=False, needed_vaccine=stock.vaccine_name).order_by('reg_date')
            for needy in needies:
                if count == 0:
                    break
                print('Mailing ', needy.email)
                send_mail(
             #SUBJECT
             f'Vaccine is available',
             #BODY
             f'''
             Email Content
             ''',
             #FROM
             'aflahvk2527@gmail.com',
             #TO
             [needy.email],
             fail_silently=False,
         )
                needy.is_mailed = True 
                needy.save()
                count -= 1
            new_stock.count += old_count
            new_stock.save()
            return redirect('/vaccine/stock')
    return render(request, 'stocks/update_vaccine.html', context={"form":form})
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from stocks.forms import BloodStockCreateForm, VaccineStockCreateForm
from stocks.models import BloodStock, VaccineStock

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
    form = BloodStockCreateForm(instance=stock)
    if request.POST:
        form = BloodStockCreateForm(request.POST, instance=stock)
        if form.is_valid():
            new_stock = form.save(commit=False)
            new_count = new_stock.count
            new_stock.count += old_count
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
    form = VaccineStockCreateForm(instance=stock)
    if request.POST:
        form = VaccineStockCreateForm(request.POST, instance=stock)
        if form.is_valid():
            new_stock = form.save(commit=False)
            new_count = new_stock.count
            new_stock.count += old_count
            new_stock.save()
            return redirect('/vaccine/stock')
    return render(request, 'stocks/update_vaccine.html', context={"form":form})
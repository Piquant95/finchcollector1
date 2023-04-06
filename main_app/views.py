from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Upgrade
from .forms import UpdatesForm

# Create your views here.



def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {
        'cars': cars
    })

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    id_list = car.upgrade.all().values_list('id')
    upgrade_car_doesnt_have = Upgrade.objects.exclude(id__in=id_list)
    updates_form = UpdatesForm()
    return render(request, 'cars/detail.html', {
        'car': car , 'updates_form' : updates_form, 'upgrade' : upgrade_car_doesnt_have
    })

class CarCreate(CreateView):
    model = Car
    fields = ['make', 'model', 'year', 'description']

class CarUpdate(UpdateView):
  model = Car
  fields = ['model', 'year', 'description']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars'


def add_updates(request, car_id):
   form = UpdatesForm(request.POST)
   
   if form.is_valid():
    new_updates = form.save(commit=False)
    new_updates.car_id = car_id
    new_updates.save()
    return redirect('detail', car_id=car_id)
   

class UpgradeList(ListView):
  model = Upgrade

class UpgradeDetail(DetailView):
  model = Upgrade

class UpgradeCreate(CreateView):
  model = Upgrade
  fields = '__all__'

class UpgradeUpdate(UpdateView):
  model = Upgrade
  fields = ['name', 'description']

class UpgradeDelete(DeleteView):
  model = Upgrade
  success_url = '/upgrade'



def assoc_upgrade(request, car_id, upgrade_id):
  
  Car.objects.get(id=car_id).upgrade.add(upgrade_id)
  return redirect('detail', car_id=car_id)


def delete_upgrade(request, car_id, upgrade_id):
  Car.objects.get(id=car_id).upgrade.remove(upgrade_id)
  return redirect('detail', car_id=upgrade_id )

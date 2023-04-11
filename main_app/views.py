from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import State, Upgrade
from .forms import UpdatesForm

# Create your views here.



def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def states_index(request):
    states = State.objects.all()
    return render(request, 'states/index.html', {
        'states': states
    })

def states_detail(request, state_id):
    state = State.objects.get(id=state_id)
    id_list = state.upgrade.all().values_list('id')
    upgrade_state_doesnt_have = Upgrade.objects.exclude(id__in=id_list)
    updates_form = UpdatesForm()
    return render(request, 'states/detail.html', {
        'state': state , 'updates_form' : updates_form, 'upgrade' : upgrade_state_doesnt_have
    })

class StateCreate(CreateView):
    model = State
    fields = ['name', 'football', 'basketball', 'baseball']

class StateUpdate(UpdateView):
  model = State
  fields = ['football', 'basketball', 'baseball']

class StateDelete(DeleteView):
  model = State
  success_url = '/states'


def add_updates(request, state_id):
   form = UpdatesForm(request.POST)
   
   if form.is_valid():
    new_updates = form.save(commit=False)
    new_updates.state_id = state_id
    new_updates.save()
    return redirect('detail', state_id=state_id)
   

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



def assoc_upgrade(request, state_id, upgrade_id):
  
  State.objects.get(id=state_id).upgrade.add(upgrade_id)
  return redirect('detail', state_id=state_id)


def delete_upgrade(request, state_id, upgrade_id):
  State.objects.get(id=state_id).upgrade.remove(upgrade_id)
  return redirect('detail', state_id=upgrade_id )

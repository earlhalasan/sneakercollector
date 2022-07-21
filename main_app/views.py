from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Sneaker, Purpose
from .forms import ReleaseForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sneakers_index(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'sneakers/index.html', {'sneakers': sneakers})

def sneakers_detail(request, sneaker_id):
    sneaker = Sneaker.objects.get(id=sneaker_id)
    id_list = sneaker.purposes.all().values_list('id')
    purposes_sneaker_doesnt_have = Purpose.objects.exclude(id__in=id_list)
    release_form = ReleaseForm()
    return render(request, 'sneakers/detail.html', {'sneaker': sneaker, 'release_form': release_form, 'purposes': purposes_sneaker_doesnt_have})

def add_release(request, sneaker_id):
      # create a ModelForm instance using the data in request.POST
  form = ReleaseForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_release = form.save(commit=False)
    new_release.sneaker_id = sneaker_id
    new_release.save()
    return redirect('detail', sneaker_id=sneaker_id)

class SneakerCreate(CreateView):
    model = Sneaker
    fields = "__all__"

class SneakerUpdate(UpdateView):
    model = Sneaker
    fields = ['brand', 'model', 'description', 'year']

class SneakerDelete(DeleteView):
    model = Sneaker
    success_url = '/sneakers/'

class PurposeList(ListView):
    model = Purpose

class PurposeDetail(DetailView):
    model = Purpose

class PurposeCreate(CreateView):
    model = Purpose
    fields = "__all__"

class PurposeUpdate(UpdateView):
    model = Purpose
    fields = ['purpose']

class PurposeDelete(DeleteView):
    model = Purpose
    success_url = '/purposes/'

def assoc_purpose(request, sneaker_id, purpose_id):
  Sneaker.objects.get(id=sneaker_id).purposes.add(purpose_id)
  return redirect('detail', sneaker_id=sneaker_id)

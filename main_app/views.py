from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm
from django.shortcuts import render, redirect
from .models import Finch, Toy
from django.views.generic import ListView, DetailView

# Create your views here.



# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

  # Add new view
def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches': finches })
  
def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form, 'toys': toys_finch_doesnt_have })

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('finches_detail', finch_id=finch_id)

def assoc_toy(request, finch_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('finches_detail', finch_id=finch_id)

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy



class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  success_url = '/finches/'
  fields = ['name', 'breed', 'description', 'age']

class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a finch by excluding the name field!
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'


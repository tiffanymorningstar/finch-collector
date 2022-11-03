from django.shortcuts import render

# Create your views here.

# Add the following import
from django.http import HttpResponse

class Finch:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('House finch', 'red', 'Kinda rude.', 3),
  Finch('American Goldfinch', 'yellow', 'Looks like a turtle.', 0),
  Finch('Purple finch', 'purple', 'Happy fluff ball.', 4),
  Finch('European Goldfinch', 'brown', 'Meows loudly.', 6)
]


# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

  # Add new view
def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })



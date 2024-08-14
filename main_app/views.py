from django.shortcuts import render
# Import HttpResponse to send text-based responses
from .models import Cat




# Create your views here.
def about(request):
    return render(request, 'about.html')

def cat_index(request):
    # Render the cats/index.html template with the cats data
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

def home(request):
    return render(request, 'home.html')

# views.py

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})

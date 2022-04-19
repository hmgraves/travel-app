from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Destination, Attraction

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def destinations_index(request):
	destinations = Destination.objects.all()
	return render(request, 'destinations/index.html', {'destinations': destinations})

def destinations_detail(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    return render(request, 'destinations/detail.html', {'destination': destination})

def attractions_detail(request, destination_id, attraction_id):
    destination = Destination.objects.get(id=destination_id)
    attraction = Attraction.objects.get(id=attraction_id)
    return render(request, 'destinations/attractions/detail.html', {'destination': destination, "attractions_detail": attractions_detail})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

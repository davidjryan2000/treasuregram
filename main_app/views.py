from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Treasure
from .forms import TreasureForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    treasures = Treasure.objects.all()
    form = TreasureForm()
    return render(request, 'index.html', {'treasures':treasures, 'form':form})

def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})

def post_treasure(request):
    form = TreasureForm(request.POST, request.FILES)
    treasure = form.save(commit = False)
    treasure.user=request.user
    treasure.save()
    if form.is_valid():
        form.save(commit=True)
     
    return HttpResponseRedirect('/')

def profile(request, username):
    user = User.objects.get(username=username)
    treasures = Treasure.objects.filter(user=user)
    return render(request,'profile.html', {'username':username,'treasures': treasures})
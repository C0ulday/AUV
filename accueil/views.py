from django.shortcuts import render
from accueil.models import Member

# Create your views here.
def index(request):
    return render(request,'accueil.html',context={})

def connexion(request):
    return render(request,'monespace.html',context={})

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'accueil.html',context={})

def connexion(request):
    return render(request,'monespace.html',context={})


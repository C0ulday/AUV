from django.shortcuts import render


# Create your views here.
def accueil(request):
    return render(request,'accueil.html',context={})

def connexion(request):
    return render(request,'monespace.html',context={})

def volsDecouverte(request):
    return render(request,'volsdecouverte.html',context={})
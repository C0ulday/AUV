from django.shortcuts import render
from accueil.models import Member

# Create your views here.
def index(request):
    return render(request,'accueil.html',context={})

def connexion(request):
    return render(request,'monespace.html',context={})

def connexionEspace(request):
    context = {}
    if request.method == "POST":
        identifiant = request.POST.get('identifiant')
        password = request.POST.get('password')

        user = Member.objects.filter(email=identifiant, password=password).first()

        if user:
            request.session['user_id'] = user.id
           # return redirect('intranet_home')  # redirige vers l'app intranet
        else:
            context['error'] = "Identifiant ou mot de passe incorrect"

    return render(request, 'accueil/monespace.html', context)
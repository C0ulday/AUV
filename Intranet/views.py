#Imports externes
from django.shortcuts import render,\
                                redirect
from django.contrib.auth import logout
from datetime import datetime

#Imports internes
from Intranet.forms import loginForm

from Intranet.models import Member

from ULMASSO.views import dateTimeParis
#************************************************************************************************************

#Gestion des sessions
    #Récupération du loggedMember de la session
def getLoggedMemberFromRequest(request):
    if 'loggedMemberId' in request.session:
        loggedMemberId = request.session['loggedMemberId']
        loggedMember = Member.objects.get(id=loggedMemberId)
        return loggedMember
    else:
        return None

    #Se connecter
def intranetLogin(request):
    templateName = "intranetLogin.html"
    context = {
        'current_date_time' : dateTimeParis(),
        'current_year' : datetime.now().year,
    }
    if len(request.POST) > 0 :
        form = loginForm(request.POST)
        if form.is_valid():
            email = request.POST['identifiant']
            password = request.POST['password'] 
            if email and password:
                result = Member.objects.filter(email=email,
                                               password = password)
                if len(result) != 1:
                    error = 'Identifiant ou mot de passe erroné'
                    context['error'] = error
                    context['form'] = form
                else:
                    loggedMember = Member.objects.get(email=email)
                    request.session['loggedMemberId'] = loggedMember.id
                    intranetAccueil(request)
                    context['loggedMember'] = loggedMember
                    templateName = 'intranetAccueil.html'
        else:
            form = loginForm()
            context['form'] = form
    else:
        form = loginForm()
        context['form'] = form
    return render(request,templateName, context)

    #Se déconnecter
def intranetDeconnect(request):
    logout(request)
    return redirect('internetAccueil')

#************************************************************************************************************

#Accueil
def intranetAccueil(request):
    loggedMember = getLoggedMemberFromRequest(request)
    if loggedMember:
        templateName = "intranetAccueil.html"
        context = {
                'current_date_time' : dateTimeParis(),
                'current_year' : datetime.now().year,
                'loggedMember' : loggedMember,
            }               
        return render(request,templateName, context)
    else:
        return redirect('/internetAccueil')

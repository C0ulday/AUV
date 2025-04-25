#Imports externes
from django.shortcuts import render,\
                            redirect,\
                            HttpResponseRedirect

#Imports internes
from intranet.views import getLoggedMemberFromRequest
from intranet.models import Aeronef
from intranet.MenuAeronef.forms import gererAeronefForm
                                                            
#************************************************************************************************************
#Aeronefs/Paramètres
    #Créer aéronef
def intranetAeronefCreate(request):
    loggedMember = getLoggedMemberFromRequest(request)
    if loggedMember:
        templateName = 'intranetAeronefCreate.html'
        context = {'loggedMember' : loggedMember,
                   'current_date_time' : 'dateTimeParis()',
                   'actionBtnName' : 'Créer ULM',
                   }
        listAeronef = Aeronef.objects.all()
        context['listAeronef'] = listAeronef
        if request.method == 'POST':
            form = gererAeronefForm(request.POST)
            if form.is_valid():
                if listAeronef:
                    typeULM = request.POST.get('type')
                    activeAeronefList = Aeronef.objects.filter(type = typeULM)
                    #Si l'aéronef existe, on le modifie
                    if activeAeronefList:
                        activeAeronef = activeAeronefList[0]#activeSectionList est un queryset. On récupère le premier
                        activeAeronef.typeULM = request.POST.get('type')
                        activeAeronef.classeULM = form.cleaned_data['classeULM']
                        activeAeronef.tarifPilote = request.POST.get('tarifPilote')
                        activeAeronef.tarifElevePilote = request.POST.get('tarifElevePilote')
                        activeAeronef.save()
                    #Sinon, on le crée
                    else:
                        form.save()
                #Si aucun n'existe
                else:
                    form.save()
            #Evite de créer le même objet quand on rafraichit la page
            return HttpResponseRedirect(request.path) 
        else:
            form = gererAeronefForm()
        context["form"] = form
        return render(request, templateName, context)     
    else:
        return redirect('/internetAccueil')

    #Supprimer aéronef
def intranetAeronefDelete(request, id):
    loggedMember = getLoggedMemberFromRequest(request)
    if loggedMember:
        if request.method == 'POST':
            activeAeronef = Aeronef.objects.get(pk=id)
            activeAeronef.delete()
            return HttpResponseRedirect("/intranetAeronefCreate")
    else:
        return redirect('/internetAccueil')    
    
    #Modifier aéronef
def intranetAeronefModify(request, id):
    loggedMember = getLoggedMemberFromRequest(request)
    if loggedMember:
        templateName ='intranetAeronefCreate.html'
        context = {
            'loggedMember' : loggedMember,
            'current_date_time' :dateTimeParis(),
            'actionBtnName' : 'Modifier l\'ULM',
            }
        listAeronef = Aeronef.objects.all()
        context['listAeronef'] = listAeronef
        if request.method == 'POST':
            activeAeronef = Aeronef.objects.get(pk=id)
            form = gererAeronefForm(instance = activeAeronef)
        context["form"] = form
        return render(request, templateName, context)  
    else:
        return redirect('/internetAccueil')
    

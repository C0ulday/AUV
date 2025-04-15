#Imports externes
from django.urls import path

#Imports internes
from Intranet.views import intranetLogin,\
                            intranetDeconnect,\
                            intranetAccueil
from Intranet.MenuMembres.views import memberPassword,\
                                intranetMemberAddShow,\
                                intranetMemberDelete,\
                                intranetMemberModify,\
                                intranetMemberShow
from Intranet.MenuBudget.views import intranetBudgetSectionAddShow,\
                                    intranetBudgetSectionDelete,\
                                    intranetBudgetSectionModify,\
                                    intranetBudgetProjetAddShow,\
                                    intranetBudgetProjetDelete,\
                                    intranetBudgetProjetModify,\
                                    intranetBudgetLigneAddShow,\
                                    intranetBudgetLigneDelete,\
                                    intranetBudgetLigneModify,\
                                    intranetBudgetLigneChoice,\
                                    intranetBudgetOperationAddShow,\
                                    intranetBudgetOperationDelete,\
                                    intranetBudgetOperationModify,\
                                    intranetBudgetCurrentYear,\
                                    intranetBudgetCurrentYearLigne,\
                                    intranetCompteEpargneChoice,\
                                    intranetCompteEpargneOperationAddShow,\
                                    intranetCompteEpargneOperationDelete,\
                                    intranetCompteEpargneOperationModify,\
                                    intranetBilanCompteEpargne,\
                                    intranetCompteEpargneAddShow,\
                                    intranetCompteEpargneDelete,\
                                    intranetCompteEpargneModify
from Intranet.MenuComptesPilotes.views import intranetMonVolCreate,\
                                            intranetMonVolDelete,\
                                            intranetMonVolModify,\
                                            intranetMonCarnetVol,\
                                            intranetMonComptePilote,\
                                            intranetVolCreate,\
                                            intranetVolDelete,\
                                            intranetVolModify,\
                                            intranetCarnetVolChoice,\
                                            intranetCarnetVol,\
                                            intranetComptePiloteChoice,\
                                            intranetComptePilote,\
                                            pdfComptePilote,\
                                            intranetBilanComptePilote   
from Intranet.MenuAeronef.views import intranetAeronefCreate,\
                                        intranetAeronefDelete,\
                                        intranetAeronefModify                        
urlpatterns = [
#gestion loggedMember
    #Internet/Intranet
    path('intranetLogin', intranetLogin, name = 'intranet_Login'),
    #Bouton déconnexion
    path('intranetDeconnect', intranetDeconnect, name = 'intranet_Deconnect'),
    #Bouton Modifier mot de passe
    path('memberProfile',memberPassword, name="member_Profile"),
    
#Accueil
    path('intranetAccueil',intranetAccueil, name="intranet_Accueil"),
    
#Membres    
    #Membres/Gérer Members
    path('intranetGererMembers', intranetMemberAddShow, name="intranet_Member_Add_Show"),
    path('deleteMember<int:id>', intranetMemberDelete, name = 'intranet_Member_Delete'),
    path('modifyMember<int:id>', intranetMemberModify, name = 'intranet_Member_Modify'), 
    #Membres/Visualiser Membres
    path('intranetVoirMembers', intranetMemberShow, name="intranet_Member_Show"),
    
#Budget
    #Budget/Gérer Sections
    path('intranetBudgetGererSection', intranetBudgetSectionAddShow, name="intranet_Budget_Section_Add_Show"),
    path('deleteBudgetSection<int:id>', intranetBudgetSectionDelete, name = 'intranet_Budget_Section_Delete'),
    path('modifyBudgetSection<int:id>', intranetBudgetSectionModify, name = 'intranet_Budget_Section_Modify'), 
    #Budget/Gérer Projets
    path('intranetBudgetGererProjet', intranetBudgetProjetAddShow, name="intranet_Budget_Projet_Add_Show"),        
    path('deleteBudgetProjet<int:id>', intranetBudgetProjetDelete, name = 'intranet_Budget_Projet_Delete'),
    path('modifyBudgetProjet<int:id>', intranetBudgetProjetModify, name = 'intranet_Budget_Projet_Modify'),       
    #Budget/Gérer Lignes
    path('intranetBudgetGererLigne', intranetBudgetLigneAddShow, name="intranet_Budget_Ligne_Add_Show"),   
    path('deleteBudgetLigne<int:id>', intranetBudgetLigneDelete, name = 'intranet_Budget_Ligne_Delete'),
    path('modifyBudgetLigne<int:id>', intranetBudgetLigneModify, name = 'intranet_Budget_Ligne_Modify'),     
    #Budget/Gérer Opérations
    path('intranetBudgetLigneChoice', intranetBudgetLigneChoice, name="intranet_Budget_Ligne_Choice"),
    path('intranetBudgetGererOperation<int:id>', intranetBudgetOperationAddShow, name="intranet_Budget_Operation_Add_Show"),   
    path('deleteBudgetOperation<int:id>', intranetBudgetOperationDelete, name = 'intranet_Budget_Operation_Delete'),
    path('modifyBudgetOperation<int:id>', intranetBudgetOperationModify, name = 'intranet_Budget_Operation_Modify'),                
    #Budget/Budget année en cours
    path('intranetBudgetCurrentYear', intranetBudgetCurrentYear, name = 'intranet_Budget_Current_Year'),
    #Budget/Budget année en cours par ligne
    path('intranetBudgetCurrentYearLigne', intranetBudgetCurrentYearLigne, name = 'intranet_Budget_Current_Year_Ligne'),
    #Budget/Gérer comptes épargne
    path('intranetGererCompteEpargne', intranetCompteEpargneAddShow, name="intranet_Compte_Epargne_Add_Show"),   
    path('deleteCompteEpargne<int:id>', intranetCompteEpargneDelete, name = 'intranet_Compte_Epargne_Delete'),
    path('modifyCompteEpargne<int:id>', intranetCompteEpargneModify, name = 'intranet_Compte_Epargne_Modify'),  
    #Budget/Opérations Comptes Epargne
    path('intranetCompteEpargneChoice', intranetCompteEpargneChoice, name="intranet_Compte_Epargne_Choice"),
    path('intranetCompteEpargneGererOperation<int:id>', intranetCompteEpargneOperationAddShow, name="intranet_Compte_Epargne_Operation_Add_Show"),
    path('deleteCompteEpargneOperation<int:id>', intranetCompteEpargneOperationDelete, name = 'intranet_Compte_Epargne_Operation_Delete'),
    path('modifyCompteEpargneOperation<int:id>', intranetCompteEpargneOperationModify, name = 'intranet_Compte_Epargne_Operation_Modify'),
    #Budget/Bilan Comptes Epargne
    path('intranetBilanCompteEpargne', intranetBilanCompteEpargne, name = 'intranet_Bilan_Compte_Epargne'),
    
#Compte pilote
    #Gestion par le loggedMember
        #Comptes pilotes/Gérer mes vols
            #Créer
    path('intranetMonVolCreate', intranetMonVolCreate, name = 'intranet_Mon_Vol_Create'),
            #Supprimer
    path('intranetMonVolDelete<int:id>', intranetMonVolDelete, name = 'intranet_Mon_Vol_Delete'),
            #Modifier
    path('intranetMonVolModify<int:id>', intranetMonVolModify, name = 'intranet_Mon_Vol_Modify'), 
        #Comptes pilotes/Mon Carnet de vol AUV
    path('intranetMonCarnetVol', intranetMonCarnetVol, name = 'intranet_Mon_Carnet_Vol'),
        #Comptes pilotes/Mon compte pilote
    path('intranetMonComptePilote', intranetMonComptePilote, name="intranet_Mon_Compte_Pilote"),
    #Gestion par l'administrateur du site
        #Comptes pilotes/Gérer les vols
            #Créer
    path('intranetVolCreate', intranetVolCreate, name = 'intranet_Vol_Create'),
            #Supprimer
    path('intranetVolDelete<int:id>', intranetVolDelete, name = 'intranet_Vol_Delete'),
            #Modifier
    path('intranetVolModify<int:id>', intranetVolModify, name = 'intranet_Vol_Modify'),
        #Comptes pilotes/Carnets de vol
            #Choisir carnet de vol
    path('intranetCarnetVolChoice', intranetCarnetVolChoice, name = 'intranet_Carnet_Vol_Choice'),
            #Voir carnet de vol
    path('intranetCarnetVol<int:id>', intranetCarnetVol, name="intranet_Carnet_Vol"),
        #Comptes pilotes/Comptes pilotes
            #Choisir compte pilote
    path('intranetComptePiloteChoice', intranetComptePiloteChoice, name = 'intranet_Compte_Pilote_Choice'),
            #Voir compte pilote
    path('intranetComptePilote<int:id>', intranetComptePilote, name="intranet_Compte_Pilote"),
            #générer pdf compte pilote
    path('pdfComptePilote<int:id>', pdfComptePilote, name="pdf_Compte_Pilote"),    
        #Comptes pilotes/Bilan comptes pilotes
    path('intranetBilanComptePilote', intranetBilanComptePilote, name="intranet_Bilan_Compte_Pilote"),
    
#Aéronefs
    #Aéronef/Paramètres
        #Créer
    path('intranetAeronefCreate', intranetAeronefCreate, name = 'intranet_Aeronef_Create'),
            #Supprimer
    path('intranetAeronefDelete<int:id>', intranetAeronefDelete, name = 'intranet_Aeronef_Delete'),
            #Modifier
    path('intranetAeronefModify<int:id>', intranetAeronefModify, name = 'intranet_Aeronef_Modify'),
    ]
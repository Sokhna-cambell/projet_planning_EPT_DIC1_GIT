from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, reverse
from .models import *

def LoginView(request):
	return render(request, 'registration/connexion.html')

def dashboard(request):
	error=""
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	mail = request.POST.get('email')
	mdp = request.POST.get('pass')
	if Eleve.objects.filter(email=mail,mot_de_passe=mdp).exists() :
		eleve = Eleve.objects.get(email=mail,mot_de_passe=mdp)
		return render(request, 'registration/dashboardEleve.html', {'eleve':eleve,'classe' : classe,'dept' : dept})
	elif Professeur.objects.filter(email=mail,mot_de_passe=mdp).exists() :
		prof = Professeur.objects.get(email=mail,mot_de_passe=mdp)
		return render(request, 'registration/dashboardProfesseur.html', {'prof':prof,'classe' : classe,'dept' : dept})
	elif Administrateur.objects.filter(email=mail,mot_de_passe=mdp).exists() :
		admin = Administrateur.objects.get(email=mail,mot_de_passe=mdp)
		return render(request, 'registration/dashboardAdmin.html', {'admin' : admin,'classe' : classe,'dept' : dept})
	else :
		error="Informations invalides"
		return LoginViewErreur(request,error)
	return render(request, 'registration/connexion.html')

def LoginViewErreur(request, erreur):
	if erreur:
		error=erreur
	return render(request, 'registration/connexion.html', {'error':error})

def Inscription(request):
	classe = Classe.objects.all()
	return render(request, 'registration/inscription.html', {'classe': classe})

def dashboardNouvelEleve(request):
		e=Eleve()
		e.prenom=request.POST.get('prenom')
		e.nom=request.POST.get('nom')
		e.email=request.POST.get('Email')
		e.telephone=request.POST.get('telephone')
		e.mot_de_passe=request.POST.get('mot_de_passe')
		for c in Classe.objects.all():
			if request.POST.get('classe')==c.nom_classe:
				e.classe=Classe.objects.get(nom_classe=c.nom_classe)
		e.genre=request.POST.get('genre')
		e.profil=request.FILES.get('profil')
		e.save()
		eleve = Eleve.objects.get(email=e.email,mot_de_passe=e.mot_de_passe)
		return render(request, 'registration/dashboardEleve.html', {'eleve':eleve})

def dashboardNouveauProfesseur(request):
		p=Professeur()
		p.prenom=request.POST.get('prenom')
		p.nom=request.POST.get('nom')
		p.email=request.POST.get('Email')
		p.telephone=request.POST.get('telephone')
		p.mot_de_passe=request.POST.get('mot_de_passe')
		p.genre=request.POST.get('genre')
		p.profil=request.POST.get('profil')
		p.save()
		prof = Professeur.objects.get(email=p.email,mot_de_passe=p.mot_de_passe)
		return render(request, 'registration/dashboardProfesseur.html', {'prof':prof})


def ListeEleve(request,classe,user,cle):
	c = classe
	dept = Departement.objects.all()
	prof = Professeur.objects.all()
	classe = Classe.objects.all()
	eleve = Eleve.objects.all()
	if user == 0:
		admin = Administrateur.objects.get(pk=cle)
		return render(request, 'registration/listeEleve.Admin.html', {'c':c,'admin':admin,'eleve':eleve,'classe':classe,'prof':prof,'dept':dept})
	if user == 1:
		el = Eleve.objects.get(pk=cle)
		return render(request, 'registration/listeEleve.Eleve.html', {'c':c,'eleve':el,'el':eleve,'classe':classe,'prof':prof,'dept':dept})
	if user == 2:
		pr = Professeur.objects.get(pk=cle)
		return render(request, 'registration/listeEleve.Prof.html', {'c':c,'prof':pr,'eleve':eleve,'classe':classe,'dept':dept})
	return LogoutView()

def LogoutView(request):

    return render(request, 'registration/connexion.html')

def GestionDepartement(request,cle):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.all()
	admin = Administrateur.objects.get(pk=cle)
	return render(request, 'registration/listeDepartement.html', {'prof':prof,'admin':admin,'dept':dept,'classe':classe})

def ListeProf(request,cle):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.all()
	admin = Administrateur.objects.get(pk=cle)
	return render(request, 'registration/listeProf.html', {'prof':prof,'admin':admin,'dept':dept,'classe':classe})

def ListeClasse(request,cle):
	prof = Professeur.objects.all()
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	admin = Administrateur.objects.get(pk=cle)
	return render(request, 'registration/listeClasse.html', {'prof':prof,'admin':admin,'dept':dept,'classe':classe})

def ProfilEleve(request,cle):
	classe = Classe.objects.all()
	prof = Professeur.objects.all()
	dept = Departement.objects.all()
	el = Eleve.objects.get(pk=cle)
	return render(request, 'registration/profilEleve.html', {'eleve':el,'prof':prof,'dept':dept,'classe':classe})

def ProfilProf(request,cle):
	eleve = Eleve.objects.all()
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	pr = Professeur.objects.get(pk=cle)
	return render(request, 'registration/profilProf.html', {'prof':pr,'dept':dept,'classe':classe,'eleve':eleve})
def listeEleves(request,user,cleUser):
	user = user
	cleUser = cleUser
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.all()
	eleve = Eleve.objects.all()
	if user == 1:
		el = Eleve.objects.get(pk=cleUser)
		return render(request, 'registration/listesEleve.Eleve.html', {'classe':classe,'user':user,'cleUser':cleUser,'eleve':el,'prof':prof,'dept':dept})
	if user == 2:
		pr = Professeur.objects.get(pk=cleUser)
		return render(request, 'registration/listesEleve.Prof.html', {'classe':classe,'user':user,'cleUser':cleUser,'eleve':eleve,'prof':pr,'dept':dept})
	if user == 0:
		admin = Administrateur.objects.get(pk=cleUser)
		return render(request, 'registration/listesEleve.Admin.html', {'classe':classe,'user':user,'cleUser':cleUser,'eleve':eleve,'prof':prof,'dept':dept,'admin':admin})
def CahierDeTexte(request,user,cleUser):
	user = user
	cleUser = cleUser
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.all()
	eleve = Eleve.objects.all()
	if user == 1:
		el = Eleve.objects.get(pk=cleUser)
		return render(request, 'registration/CDT.Eleve.html', {'classe':classe,'user':user,'cleUser':cleUser,'eleve':el,'prof':prof,'dept':dept})
	if user == 2:
		pr = Professeur.objects.get(pk=cleUser)
		return render(request, 'registration/CDT.Prof.html', {'classe':classe,'user':user,'cleUser':cleUser,'eleve':eleve,'prof':pr,'dept':dept})

def CahierDeTexteClasse(request,user,cleUser,cleClasse):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.all()
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	if user == 1:
		el = Eleve.objects.get(pk=cleUser)
		return render(request, 'registration/CDTClasse.Eleve.html', {'classe':classe,'cl':cl,'eleve':el,'prof':prof,'dept':dept})
	if user == 2:
		pr = Professeur.objects.get(pk=cleUser)
		return render(request, 'registration/CDTClasse.Prof.html', {'classe':classe,'cl':cl,'prof':pr,'dept':dept,'eleve':eleve})
	return LogoutView()

def EmploiDuTemps(request,user,cleUser):
	user = user
	cleUser = cleUser
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.all()
	eleve = Eleve.objects.all()
	if user == 1:
		el = Eleve.objects.get(pk=cleUser)
		return render(request, 'registration/EDT.Eleve.html', {'classe':classe,'user':user,'cleUser':cleUser,'eleve':el,'prof':prof,'dept':dept})
	if user == 2:
		pr = Professeur.objects.get(pk=cleUser)
		return render(request, 'registration/EDT.Prof.html', {'classe':classe,'user':user,'cleUser':cleUser,'eleve':eleve,'prof':pr,'dept':dept})
	return LogoutView()

def EmploiDuTempsClasse(request,user,cleUser,cleClasse):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.all()
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	caseModule = CaseModule.objects.all()
	nbreCM = caseModule.count()
	caseMatiere = CaseMatiere.objects.all()
	module = Module.objects.all()
	matiere = Matiere.objects.all()
	case = "vide"
	jours = Jour.objects.all()
	heuresMatin = range(8,12)
	heuresSoir = range(15,19)
	if user == 1:
		el = Eleve.objects.get(pk=cleUser)
		return render(request, 'registration/EDTClasse.Eleve.html', {'Module':module,'Matiere':matiere,'classe':classe,'cl':cl,'eleve':el,'prof':prof,'dept':dept,'caseModule':caseModule,'caseMatiere':caseMatiere,'case':case,'jours':jours,'heuresMatin':heuresMatin,'heuresSoir':heuresSoir,'nbreCM':nbreCM})
	if user == 2:
		pr = Professeur.objects.get(pk=cleUser)
		return render(request, 'registration/EDTClasse.Prof.html', {'Module':module,'Matiere':matiere,'classe':classe,'cl':cl,'prof':pr,'dept':dept,'eleve':eleve,'caseModule':caseModule,'caseMatiere':caseMatiere,'case':case,'jours':jours,'heuresMatin':heuresMatin,'heuresSoir':heuresSoir,'nbreCM':nbreCM})
	return LogoutView()

def newEDT(request,cleUser,cleClasse):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.all()
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	module = Module.objects.all()
	matiere = Matiere.objects.all()
	caseModule = CaseModule.objects.all()
	nbreCM = caseModule.count()
	caseMatiere = CaseMatiere.objects.all()
	case = "vide"
	jours = Jour.objects.all()
	heuresMatin = range(8,12)
	heuresSoir = range(15,19)
	pr = Professeur.objects.get(pk=cleUser)
	if request.POST:
		for i in heuresMatin or i in heuresSoir:
			for j in jours:
				if cl.departement.systeme == "lmd":
					found = False
					for c in caseModule:
						if c.module.classe.nom_classe == cl.nom_classe and c.heure_debut == i and c.jour == j:
							found = True
							c.delete()
							if request.POST.get('{} {}'.format(j.nom,i)) == "vide":
								break
							else:
								newC = CaseModule()
								nom_module = request.POST.get('{} {}'.format(j.nom,i))
								newC.module = Module.objects.get(nom=nom_module)
								newC.jour = j
								newC.heure_debut = i
								newC.save()
					if found == False:
						if request.POST.get('{} {}'.format(j.nom,i)) == "vide":
							break
						else:
							newC = CaseModule()
							nom_module = request.POST.get('{} {}'.format(j.nom,i))
							newC.module = Module.objects.get(nom=nom_module)
							newC.jour = j
							newC.heure_debut = i
							newC.save()
				elif cl.departement.systeme == "semestriel":
					found = False
					for c in caseMatiere:
						if c.matiere.classe.nom_classe == cl.nom_classe and c.heure_debut == i and c.jour == j:
							found = True
							if request.POST.get('{} {}'.format(j.nom,i)) == "vide":
								c.delete()
							else:
								nom_matiere = request.POST.get('{} {}'.format(j.nom,i))
								c.matiere = Matiere.objects.get(nom=nom_matiere)
								c.save()
					if found == False:
						if request.POST.get('{} {}'.format(j.nom,i)) == "vide":
							break
						else:
							newC = CaseMatiere()
							nom_matiere = request.POST.get('{} {}'.format(j.nom,i))
							newC.matiere = Matiere.objects.get(nom=nom_matiere)
							newC.jour = j
							newC.heure_debut = i
							newC.save()

	return render(request, 'registration/EDTClasse.Prof.html', {'Module':module,'Matiere':matiere,'classe':classe,'cl':cl,'prof':pr,'dept':dept,'eleve':eleve,'caseModule':caseModule,'caseMatiere':caseMatiere,'case':case,'jours':jours,'heuresMatin':heuresMatin,'heuresSoir':heuresSoir,'nbreCM':nbreCM})

def Maquette(request,user,cleUser):
	user = user
	cleUser = cleUser
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.all()
	eleve = Eleve.objects.all()
	if user == 1:
		el = Eleve.objects.get(pk=cleUser)
		return render(request, 'registration/maquette.Eleve.html', {'classe':classe,'user':user,'cleUser':cleUser,'eleve':el,'prof':prof,'dept':dept})
	if user == 2:
		pr = Professeur.objects.get(pk=cleUser)
		return render(request, 'registration/maquette.Prof.html', {'classe':classe,'user':user,'cleUser':cleUser,'eleve':eleve,'prof':pr,'dept':dept})
	return LogoutView()


def MaquetteClasse(request,user,cleUser,cleClasse):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.all()
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	ue = UE.objects.all()
	matiere = Matiere.objects.all()
	module = Module.objects.all()
	if cl.departement.systeme == 'lmd':
		for m in module:
			m.total = m.CM + m.TD_TP
			m.save()
		for u in ue:
			u.total_ECTS = 0
			u.total_coef = 0
			u.nbre_modules = 0
			for m in module: 
				if m.UE == u and m.classe.nom_classe == cl.nom_classe :
					u.total_ECTS += m.ECTS
					u.total_coef += m.coef 
					u.nbre_modules += 1
				u.save()
		totalCH=0
		totalTPE=0
		totalECTS=0
		totalCoef=0
		for m in module :
			if m.classe.nom_classe == cl.nom_classe :
				totalCH += m.total
				totalTPE += m.TPE 
				totalECTS += m.ECTS
				totalCoef += m.coef

		if user == 1:
			el = Eleve.objects.get(pk=cleUser)
			return render(request, 'registration/maquetteClasse.Eleve.html', {'classe':classe,'cl':cl,'eleve':el,'prof':prof,'dept':dept, 'UE':ue, 'matiere':matiere, 'module':module, 'totalCH':totalCH, 'totalTPE':totalTPE, 'totalECTS':totalECTS, 'totalCoef':totalCoef})
		if user == 2:
			pr = Professeur.objects.get(pk=cleUser)
			return render(request, 'registration/maquetteClasse.Prof.html', {'classe':classe,'cl':cl,'prof':pr,'dept':dept,'eleve':eleve, 'UE':ue, 'matiere':matiere, 'module':module, 'totalCH':totalCH, 'totalTPE':totalTPE, 'totalECTS':totalECTS, 'totalCoef':totalCoef})

	elif cl.departement.systeme == 'semestriel':
		matieres_sem1 = 0
		total_coef_sem1 = 0
		matieres_sem2 = 0
		total_coef_sem2 = 0
		totalCH = 0
		totalCoef = 0
		for m in matiere:
			if m.classe == cl:
				if m.semestre == 1: 
					matieres_sem1 += 1
					total_coef_sem1 += m.coef
					totalCH += m.charge_horaire
					totalCoef += m.coef
				elif m.semestre == 2: 
					matieres_sem2 += 1
					total_coef_sem2 += m.coef
					totalCH += m.charge_horaire
					totalCoef += m.coef
		if user == 1:
			el = Eleve.objects.get(pk=cleUser)
			return render(request, 'registration/maquetteClasse.Eleve.html', {'classe':classe,'cl':cl,'eleve':el,'prof':prof,'dept':dept, 'UE':ue, 'matiere':matiere, 'module':module, 'totalCH':totalCH, 'totalCoef':totalCoef, 'total_coef_sem1':total_coef_sem1, 'total_coef_sem2':total_coef_sem2, 'matieres_sem1':matieres_sem1, 'matieres_sem2':matieres_sem2})
		if user == 2:
			pr = Professeur.objects.get(pk=cleUser)
			return render(request, 'registration/maquetteClasse.Prof.html', {'classe':classe,'cl':cl,'prof':pr,'dept':dept,'eleve':eleve, 'UE':ue, 'matiere':matiere, 'module':module, 'totalCH':totalCH, 'totalCoef':totalCoef, 'total_coef_sem1':total_coef_sem1, 'total_coef_sem2':total_coef_sem2, 'matieres_sem1':matieres_sem1, 'matieres_sem2':matieres_sem2})
	return LogoutView()

def AddUE (request,cleUser,cleClasse):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.get(pk=cleUser)
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	ue = UE.objects.all()
	return render(request, 'registration/addUE.html', {'classe':classe,'cl':cl,'prof':prof,'dept':dept,'eleve':eleve, 'UE':ue})

def AddMatiere (request,cleUser,cleClasse):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.get(pk=cleUser)
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	matiere = Matiere.objects.all()
	return render(request, 'registration/addMatiere.html', {'classe':classe,'cl':cl,'prof':prof,'dept':dept,'eleve':eleve, 'matiere':matiere})

def AddModule (request,cleUser,cleClasse):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.get(pk=cleUser)
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	module = Module.objects.all() 
	ue = UE.objects.all()
	return render(request, 'registration/addModule.html', {'classe':classe,'cl':cl,'prof':prof,'dept':dept,'eleve':eleve, 'module':module, 'UE':ue})
	

def EditUE (request,cleUser,cleClasse, cleUE):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.get(pk=cleUser)
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	ue = UE.objects.get(pk=cleUE)
	return render(request, 'registration/editUE.html', {'classe':classe,'cl':cl,'prof':prof,'dept':dept,'eleve':eleve, 'UE':ue})

def EditModule (request,cleUser,cleClasse, cleModule):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.get(pk=cleUser)
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	module = Module.objects.get(pk=cleModule)
	ue = UE.objects.all()
	return render(request, 'registration/editModule.html', {'classe':classe,'cl':cl,'prof':prof,'dept':dept,'eleve':eleve, 'module':module, 'UE':ue})

def EditMatiere (request,cleUser,cleClasse, cleMatiere):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.get(pk=cleUser)
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	matiere = Matiere.objects.get(pk=cleMatiere)
	return render(request, 'registration/editMatiere.html', {'classe':classe,'cl':cl,'prof':prof,'dept':dept,'eleve':eleve, 'matiere':matiere})

def SaveUE (request,cleUser,cleClasse, cleUE):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.get(pk=cleUser)
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	module =Module.objects.all()
	matiere = Matiere.objects.all()
	if cleUE == 0:
		ue = UE.objects.all()
		new_UE=UE()
		new_UE.nom=request.POST.get('nom')
		new_UE.codeUE=request.POST.get('codeUE')
		new_UE.departement=cl.departement
		new_UE.save()
		return MaquetteClasse(request, 2, cleUser, cleClasse)
	ue = UE.objects.get(pk=cleUE)
	ue.nom = request.POST.get('nom')
	ue.codeUE = request.POST.get('codeUE')
	ue.save()
	return MaquetteClasse(request, 2, cleUser, cleClasse)

def SaveModule (request,cleUser,cleClasse, cleModule):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.get(pk=cleUser)
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	matiere = Matiere.objects.all()
	ue = UE.objects.all()
	if cleModule == 0 :
		module = Module.objects.all()
		new_module=Module()
		new_module.nom=request.POST.get('nom')
		u=request.POST.get('UE')
		new_module.UE=ue.get(nom=u)
		new_module.CM=request.POST.get('CM')
		new_module.TD_TP=request.POST.get('TD_TP')
		new_module.TPE=request.POST.get('TPE')
		new_module.ECTS=request.POST.get('ECTS')
		new_module.coef=request.POST.get('coef')
		new_module.classe=cl
		new_module.save()
		return MaquetteClasse(request, 2, cleUser, cleClasse)
	module = Module.objects.get(pk=cleModule)
	module.nom=request.POST.get('nom')
	module.UE=ue.get(nom=request.POST.get('UE'))
	module.CM=request.POST.get('CM')
	module.TD_TP=request.POST.get('TD_TP')
	module.TPE=request.POST.get('TPE')
	module.ECTS=request.POST.get('ECTS')
	module.coef=request.POST.get('coef')
	module.save()
	return MaquetteClasse(request, 2, cleUser, cleClasse)

def SaveMatiere (request,cleUser,cleClasse, cleMatiere):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.get(pk=cleUser)
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	module = Module.objects.all()
	ue = UE.objects.all()   
	if cleMatiere == 0:
		matiere = Matiere.objects.all()
		new_matiere=Matiere()
		new_matiere.nom=request.POST.get('nom')
		new_matiere.semestre=request.POST.get('semestre')
		new_matiere.coef=request.POST.get('coef')
		new_matiere.charge_horaire=request.POST.get('charge_horaire')
		new_matiere.classe=cl
		new_matiere.save()
		return MaquetteClasse(request, 2, cleUser, cleClasse)
	matiere = Matiere.objects.get(pk=cleMatiere)
	matiere.nom = request.POST.get('nom')
	matiere.semestre = request.POST.get('semestre')
	matiere.coef = request.POST.get('coef')
	matiere.charge_horaire = request.POST.get('charge_horaire')
	matiere.save()
	return MaquetteClasse(request, 2, cleUser, cleClasse)

def DeleteUE (request,cleUser,cleClasse, cleUE):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.get(pk=cleUser)
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	module = Module.objects.all()
	matiere = Matiere.objects.all()
	ue = UE.objects.get(pk=cleUE)
	ue.delete()
	return MaquetteClasse(request, 2, cleUser, cleClasse)

def DeleteMatiere (request,cleUser,cleClasse, cleMatiere):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.get(pk=cleUser)
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	module = Module.objects.all()
	matiere = Matiere.objects.get(pk=cleMatiere)
	ue = UE.objects.all()
	matiere.delete()
	return MaquetteClasse(request, 2, cleUser, cleClasse)

def DeleteModule (request,cleUser,cleClasse, cleModule):
	classe = Classe.objects.all()
	dept = Departement.objects.all()
	prof = Professeur.objects.get(pk=cleUser)
	eleve = Eleve.objects.all()
	cl = Classe.objects.get(pk=cleClasse)
	ue = UE.objects.all()
	matiere = Matiere.objects.all()
	module = Module.objects.get(pk=cleModule)
	module.delete()
	return MaquetteClasse(request, 2, cleUser, cleClasse)
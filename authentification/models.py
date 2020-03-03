from django.db import models

class Author(models.Model):
    nom = models.CharField(max_length=40)
    mdp = models.CharField(max_length=40)

class Departement(models.Model):
    nom_dept = models.CharField('nom_dept', max_length=30)
    systeme = models.CharField('nom_dept', max_length=30, default='semestriel')
    chef_dept = models.ForeignKey('Professeur',on_delete=models.CASCADE, default="1")

class Classe(models.Model):
    nom_classe = models.CharField('nom_classe', max_length=10)
    departement = models.ForeignKey('Departement', on_delete=models.CASCADE)


class Eleve(models.Model):
    prenom = models.CharField(max_length=40)
    nom = models.CharField(max_length=20)
    email = models.EmailField(unique=True, null=False)
    telephone = models.IntegerField()
    statut = models.CharField(default='simple', max_length=40)
    genre = models.CharField(max_length=20, default='genre')
    profil = models.ImageField(upload_to="photos/",default='/media/photos/avatar1.png/')
    mot_de_passe = models.CharField(null=False, max_length=40)
    classe = models.ForeignKey('Classe',on_delete=models.CASCADE)

class Professeur(models.Model):
    prenom = models.CharField(max_length=40)
    nom = models.CharField(max_length=20)
    email = models.EmailField(unique=True, null=False)
    telephone = models.IntegerField()
    respClasse = models.CharField(default='Non', max_length=40)
    respDept = models.CharField(default='Non', max_length=40)
    genre = models.CharField(max_length=20, default='genre',null=True)
    profil = models.ImageField(upload_to="photos/",default='/media/photos/avatar1.png/')
    mot_de_passe = models.CharField(null=False, max_length=40)
    

class Administrateur(models.Model):
    email = models.EmailField('Email', unique=True, null=False)
    mot_de_passe = models.CharField('mot_de_passe', null=False, max_length=40)

class UE(models.Model):
    nom=models.CharField(max_length=40)
    codeUE=models.CharField(max_length=40)
    departement = models.ForeignKey('Departement', on_delete=models.CASCADE)
    total_ECTS = models.IntegerField(default=0)
    total_coef = models.IntegerField(default=0)
    nbre_modules = models.IntegerField(default=0)

class Module(models.Model):
    nom=models.CharField(max_length=40)
    CM=models.IntegerField()
    TD_TP=models.IntegerField()
    TPE=models.IntegerField()
    ECTS=models.IntegerField()
    coef=models.IntegerField()
    classe = models.ForeignKey('Classe',on_delete=models.CASCADE)
    UE = models.ForeignKey('UE',on_delete=models.CASCADE)
    total = models.IntegerField(default=0)

class Matiere(models.Model):
    nom=models.CharField(max_length=40)
    semestre=models.IntegerField()
    coef=models.IntegerField()
    charge_horaire = models.IntegerField()
    classe = models.ForeignKey('Classe',on_delete=models.CASCADE)

class CaseModule (models.Model):
    module = models.ForeignKey('Module',on_delete=models.CASCADE)
    jour = models.ForeignKey('Jour',on_delete=models.CASCADE)
    heure_debut = models.IntegerField()
    

class CaseMatiere (models.Model):
    matiere = models.ForeignKey('Matiere',on_delete=models.CASCADE)
    jour = models.ForeignKey('Jour',on_delete=models.CASCADE)
    heure_debut = models.IntegerField()
    

class Jour(models.Model):
    nom = models.CharField(max_length=20)
    commentaire = models.CharField(max_length=200,default="Jour non commenté")
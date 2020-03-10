from django.contrib import admin
from .models import *
from .models import Author

class EleveAdmin(admin.ModelAdmin):
	list_display=('prenom','nom','email','telephone','statut','genre','profil','mot_de_passe','classe')

class ProfesseurAdmin(admin.ModelAdmin):
	list_display=('prenom','nom','email','telephone','respClasse','respDept','genre','profil','mot_de_passe')

class ClasseAdmin(admin.ModelAdmin):
	list_display=('nom_classe','departement','respClasse')

class DepartementAdmin(admin.ModelAdmin):
	list_display=('nom_dept','systeme','chef_dept')

class AdministrateurAdmin(admin.ModelAdmin):
	list_display=('email','mot_de_passe')

class UEAdmin(admin.ModelAdmin):
	list_display=('nom','codeUE','departement','total_ECTS','total_coef')

class ModuleAdmin(admin.ModelAdmin):
	list_display=('nom','CM','TD_TP','TPE','ECTS','coef','classe','UE','total')

class MatiereAdmin(admin.ModelAdmin):
	list_display=('nom','semestre','coef','charge_horaire','classe')

class CaseModuleAdmin (admin.ModelAdmin):
	list_display=('module','jour','heure_debut')

class CaseMatiereAdmin (admin.ModelAdmin):
	list_display=('matiere','jour','heure_debut')

class JourAdmin (admin.ModelAdmin):
	list_display=('nom','commentaire')

admin.site.register(Eleve, EleveAdmin)
admin.site.register(Professeur, ProfesseurAdmin)
admin.site.register(Classe, ClasseAdmin)
admin.site.register(Departement, DepartementAdmin)
admin.site.register(Administrateur, AdministrateurAdmin)
admin.site.register(UE, UEAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Matiere, MatiereAdmin)
admin.site.register(CaseModule, CaseModuleAdmin)
admin.site.register(CaseMatiere, CaseMatiereAdmin)
admin.site.register(Jour, JourAdmin)

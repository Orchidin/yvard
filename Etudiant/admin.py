from django.contrib import admin

# Register your models here. 

from . models import Etudiants

from django.contrib.admin import AdminSite

from django.contrib.auth.models import User,Group

class EtudiantAdmin(admin.ModelAdmin):
	list_display=['nom','prenom','matricule','adresse','option','niveau','description','photo']
	list_display_links=['nom','prenom','matricule','adresse','option','niveau','description','photo']
	search_fields=['nom','prenom','matricule','adresse','option','niveau','description','photo']
	list_filter=['nom','prenom','matricule','adresse','option','niveau','description','photo']
	fields=['nom','prenom','matricule','adresse','option','niveau','description','photo']


admin.site.register(Etudiants,EtudiantAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)


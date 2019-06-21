from django.shortcuts import render

from .models import Etudiants

from django.views.generic import DetailView


# Create your views here.

def etudiant(request):
	etudiants=Etudiants.objects.all()
	return render(request,"pages/etudiant.html",{'etudiants':etudiants})

def acceuil(request):
	return render(request,"pages/acceuil.html")

def profils(request):
	voir=Etudiants.objects.get(pk=id)
	return render(request,"pages/profils.html",{'voir': voir})

class Profils(DetailView):
	model=Etudiants
	template_name="pages/profils.html"

	


	
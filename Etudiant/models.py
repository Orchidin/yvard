from django.db import models
# Create your models here.


class Etudiants(models.Model):
	nom=models.CharField(max_length=15)
	prenom=models.CharField(max_length=30)
	matricule=models.CharField(max_length=8)
	adresse=models.CharField(max_length=20)
	option=models.CharField(max_length=30)
	niveau=models.CharField(max_length=5)
	description=models.TextField()
	photo=models.ImageField()
	
	def __str__(self):
		return self.nom.title()

	class Meta:
		ordering=('nom',)

	
from django.urls import path

from . import views
from .views import Profils


urlpatterns = [
    path('',views.acceuil,name="acceuil"),
    path('acceuil',views.acceuil,name="acceuil"),
    path('etudiant/',views.etudiant,name="etudiant"),
    path('profils/<int:pk>',Profils.as_view(),name="profils"),
]  
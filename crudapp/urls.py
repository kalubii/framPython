from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.personnel_form, name='home'),
    path('', views.personnel_form, name="personnel_insert"),
    path('<int:id>/', views.personnel_form, name="update"),
    path('delete/<int:id>/', views.personnel_delete, name="delete"),
    path('liste/',views.personnel_liste, name="liste")
]
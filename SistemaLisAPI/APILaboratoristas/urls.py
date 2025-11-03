from django.urls import path
from .views import LaboratoristasView  # cambia según la app

urlpatterns = [
    path('', LaboratoristasView.as_view()),
    path('<str:cod_laboratorista>/', LaboratoristasView.as_view()),
]

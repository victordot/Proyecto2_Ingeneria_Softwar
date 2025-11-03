from django.urls import path
from .views import ResultadosView

urlpatterns = [
    path('', ResultadosView.as_view()),                # GET all / POST
    path('<int:id_resultado>/', ResultadosView.as_view())  # GET, PUT, DELETE
]


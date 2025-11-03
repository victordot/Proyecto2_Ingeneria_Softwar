from django.urls import path
from .views import LoginView

urlpatterns = [
    path('', LoginView.as_view()),       # GET all / POST
    path('<int:id>/', LoginView.as_view())  # GET, PUT, DELETE por id
]


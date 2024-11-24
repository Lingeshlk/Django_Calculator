from django.urls import path, include  # Correct import
from . import views  # Import your views

urlpatterns = [
    path('', views.index, name='index'),  # Define your URL patterns using path()
]

from django.urls import path
from .views import passgen, home

urlpatterns = [
    path('', home, name='home'),
    path('generate/', passgen, name='passwordgen')
]
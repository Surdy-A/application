from django.urls import path
from .views import form_view

app_name = 'application'

urlpatterns = [
   path('', form_view, name="home")
]
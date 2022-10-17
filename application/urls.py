from django.urls import path
from .views import form_view, generatePDF, print_view

app_name = 'application'

urlpatterns = [
   path('', form_view, name="home"),
   path('print/<int:id>', generatePDF, name='generatePDF'),
   path('print/', print_view, name='print')

]
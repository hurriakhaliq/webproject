from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_form_submit/', views.contact_form_submit, name='contact_form_submit'),
]

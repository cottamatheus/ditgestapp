from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.homeditgest),
    path('inicio/login', views.login),
    path('inicio/open', views.openaccount),
    ]

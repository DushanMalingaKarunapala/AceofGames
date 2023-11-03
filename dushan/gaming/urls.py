from django.urls import path
from . import views

urlpatterns = [
    path('', views.gaming, name='gaming'),  # home page url
    path("Store/", views.Store, name= 'Store'),
    path("forza/", views.forza, name='forza')

]

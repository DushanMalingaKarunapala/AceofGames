from django.urls import path
from . import views

urlpatterns = [
    path('', views.gaming, name='gaming'),  # home page url
    

]

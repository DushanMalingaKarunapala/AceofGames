from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),  # register page for accounts app(if someone is calling for register page )
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),

]

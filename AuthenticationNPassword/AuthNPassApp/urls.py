from django.urls import path
from AuthNPassApp import views

app_name='AuthNPassApp'

urlpatterns=[
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="user_login"),
    path("menu/", views.menu, name="menu"),
    path("contacts/", views.contacts, name='contacts'),
]

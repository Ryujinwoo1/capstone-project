from django.urls import path
from secondproject import views

urlpatterns =[
    path('', views.index),
    path('login/',views.login_page),
    path('signup/',views.signup_page)
]
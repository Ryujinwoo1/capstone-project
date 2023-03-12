from django.urls import path
from secondproject import views

urlpatterns =[
    path('', views.index)
]
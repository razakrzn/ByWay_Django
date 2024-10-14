from django.urls import path
from web import views  

urlpatterns = [
    path('', views.home, name='home'), 
    path('details/', views.details, name='details'),  
]

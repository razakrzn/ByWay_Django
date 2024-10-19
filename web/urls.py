from django.urls import path
from web import views  


app_name = 'web' 

urlpatterns = [
    path('', views.home, name='home'), 
    path('course/<int:id>/', views.course_details, name='course_details'),
    path('topcourse/', views.top_courses, name='top_courses'),
]

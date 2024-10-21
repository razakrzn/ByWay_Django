from django.urls import path
from .views import home, course_details, top_courses, category_details, instructor_courses


app_name = 'web' 

urlpatterns = [
    path('', home, name='home'), 
    path('course/<int:id>/', course_details, name='course_details'),
    path('topcourse/', top_courses, name='top_courses'),
    path('category/<int:category_id>/', category_details, name='category_details'),
    path('instructor/<int:instructor_id>/', instructor_courses, name='instructor_courses'),
]

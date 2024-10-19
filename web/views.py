from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Testimonial, Categories, Instructors, Courses, Syllabus


def home(request):
    testimonials = Testimonial.objects.all()
    categories = Categories.objects.annotate(courses_count=Count('courses'))
    instructors = Instructors.objects.all()
    top_instructors = instructors[:5] 
    remaining_instructors = instructors[5:]
    courses = Courses.objects.all()
    context = {
        'testimonials': testimonials,
        'categories': categories,
        'instructors': instructors,
        'top_instructors': top_instructors,
        'remaining_instructors': remaining_instructors,
        'courses': courses
    }
    return render(request, 'home.html', context=context)  


def course_details(request, id):
    testimonials = Testimonial.objects.all()
    course = get_object_or_404(Courses, id=id)
    
    top_course = Courses.objects.first()
    
    syllabus_items = top_course.syllabus.all() if top_course else []
    
    context = {
        'course': course,
        'testimonials': testimonials,
        'syllabus_items': syllabus_items,
    }
    
    return render(request, 'details.html', context=context)


def top_courses(request):
    courses = Courses.objects.all()

    context = {
        'courses': courses
    }
    
    return render(request, 'topCourses.html', context=context)

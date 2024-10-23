from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from web.models import Testimonial, Categories, Instructors, Courses, Syllabus


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
        'top_instructors': top_instructors,
        'remaining_instructors': remaining_instructors,
        'courses': courses
    }
    
    return render(request, 'web/index.html', context=context)


def course_details(request, id):
    testimonials = Testimonial.objects.all()
    course = get_object_or_404(Courses, id=id)
    syllabi = course.syllabi.all()
    courses = Courses.objects.all()



    context = {
        'course': course,
        'testimonials': testimonials,
        'syllabi': syllabi,
        'courses': courses
    }

    return render(request, 'web/details.html', context=context)


def top_courses(request):
    courses = Courses.objects.all()

    context = {
        'courses': courses
    }
    
    return render(request, 'web/topCourses.html', context=context)


def category_details(request, category_id):
    category = get_object_or_404(Categories, id=category_id)
    courses = category.courses.all()

    return render(request, 'web/category_details.html', {'category': category, 'courses': courses})


def instructor_courses(request, instructor_id):
    instructor = get_object_or_404(Instructors, id=instructor_id)
    courses = Courses.objects.filter(instructor=instructor)
    
    context = {
        'instructor': instructor,
        'courses': courses,
    }
    return render(request, 'web/instructor_courses.html', context)
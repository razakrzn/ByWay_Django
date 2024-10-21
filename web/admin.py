from django.contrib import admin
from .models import Testimonial, Categories, Instructors, Languages, Courses, Syllabus


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'designation', 'image', 'description')


admin.site.register(Testimonial, TestimonialAdmin)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'description',)


admin.site.register(Courses, CoursesAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon',)

admin.site.register(Categories, CategoriesAdmin)


class InstructorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'designation',)


admin.site.register(Instructors, InstructorsAdmin)


admin.site.register(Languages)


admin.site.register(Syllabus)

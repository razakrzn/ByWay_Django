from django.db import models


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    description = models.TextField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=100)
    icon = models.FileField(upload_to='categories/')

    def __str__(self):
        return self.name


class Instructors(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='instructors/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    rating = models.FloatField(default=0.0)  
    students = models.IntegerField(default=0)
    courses_count = models.IntegerField(default=0)
    reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Languages(models.Model):
    languages = models.CharField(max_length=50)

    def __str__(self):
        return self.languages


class Courses(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='courses/')  
    description = models.TextField()
    certification = models.TextField()
    rating = models.FloatField(default=0.0)
    rating_count = models.IntegerField()
    duration = models.TextField()  
    instructor = models.ForeignKey('Instructors', on_delete=models.CASCADE)
    languages = models.ManyToManyField('Languages', related_name='courses')  
    price = models.DecimalField(max_digits=10, decimal_places=1) 
    discount_percent = models.DecimalField(max_digits=2, decimal_places=0, default=0.0) 
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def discounted_price(self):
        discount = (self.discount_percent / 100) * self.price
        return round(self.price - discount, 2)

    class Meta:
            ordering = ["id"]

class Syllabus(models.Model):
    top_course = models.ForeignKey(Courses, related_name='syllabus', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    lessons = models.PositiveIntegerField()
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.title



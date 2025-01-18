from django.contrib import admin
from .models import Teacher, Lesson, Assignment, Student, Permormance

# Register your models here.
admin.site.register([Teacher, Lesson, Assignment, Student, Permormance])
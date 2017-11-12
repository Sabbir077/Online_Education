from django.contrib import admin

from . models import Course, Teacher,Student,Exam,MCQ


# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Exam)
admin.site.register(MCQ)

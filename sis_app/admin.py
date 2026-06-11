from django.contrib import admin
from .models import Course, Student, Faculty, Subject, Enrollment, Exam, Result

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Subject)
admin.site.register(Enrollment)
admin.site.register(Exam)
admin.site.register(Result)
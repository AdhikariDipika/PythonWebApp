from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Students
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/edit/<int:id>/', views.student_edit, name='student_edit'),
    path('students/delete/<int:id>/', views.student_delete, name='student_delete'),

    # Courses
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_add, name='course_add'),
    path('courses/edit/<int:id>/', views.course_edit, name='course_edit'),
    path('courses/delete/<int:id>/', views.course_delete, name='course_delete'),

    # Faculty
    path('faculty/', views.faculty_list, name='faculty_list'),
    path('faculty/add/', views.faculty_add, name='faculty_add'),
    path('faculty/edit/<int:id>/', views.faculty_edit, name='faculty_edit'),
    path('faculty/delete/<int:id>/', views.faculty_delete, name='faculty_delete'),

    # Subjects
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/add/', views.subject_add, name='subject_add'),
    path('subjects/edit/<int:id>/', views.subject_edit, name='subject_edit'),
    path('subjects/delete/<int:id>/', views.subject_delete, name='subject_delete'),

    # Enrollments
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('enrollments/add/', views.enrollment_add, name='enrollment_add'),
    path('enrollments/edit/<int:id>/', views.enrollment_edit, name='enrollment_edit'),
    path('enrollments/delete/<int:id>/', views.enrollment_delete, name='enrollment_delete'),

    # Exams
    path('exams/', views.exam_list, name='exam_list'),
    path('exams/add/', views.exam_add, name='exam_add'),
    path('exams/edit/<int:id>/', views.exam_edit, name='exam_edit'),
    path('exams/delete/<int:id>/', views.exam_delete, name='exam_delete'),

    # Results
    path('results/', views.result_list, name='result_list'),
    path('results/add/', views.result_add, name='result_add'),
    path('results/edit/<int:id>/', views.result_edit, name='result_edit'),
    path('results/delete/<int:id>/', views.result_delete, name='result_delete'),
    
    # Report
    path('results/report/<int:student_id>/', views.student_report, name='student_report'),
]
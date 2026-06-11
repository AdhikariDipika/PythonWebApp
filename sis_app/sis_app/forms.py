from django import forms
from .models import Course, Student, Faculty, Subject, Enrollment, Exam, Result

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course'] # enrollment_date is auto_now_add

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'
        widgets = {
            'exam_date': forms.DateInput(attrs={'type': 'date'})
        }

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['student', 'exam', 'marks']
        # Exclude grade and grade_point as they are auto-calculated
from django.db import models
from decimal import Decimal 
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=200)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    @property
    def cgpa(self):
        total_points = Decimal('0.00')
        total_credits = 0
        
        # Fetch all results for this specific student
        results = Result.objects.filter(student=self).select_related('exam__subject')
        
        for result in results:
            subject_credits = result.exam.subject.credits
            # Multiply grade point by the credit hours of the subject
            total_points += (result.grade_point * subject_credits)
            total_credits += subject_credits
            
        if total_credits == 0:
            return Decimal('0.00')
        
            
        return round(total_points / total_credits, 2)

    # NEW: Helper to easily fetch detailed results for the dropdown/expansion UI
    @property
    def detailed_results(self):
        return Result.objects.filter(student=self).select_related('exam__subject')
    # Add this property inside your Student class in models.py
    @property
    def overall_grade(self):
        gpa = self.cgpa
        if gpa >= 3.75: return 'A+'
        elif gpa >= 3.50: return 'A'
        elif gpa >= 3.00: return 'B'
        elif gpa >= 2.50: return 'C'
        elif gpa > 0.00: return 'D'
        return 'F'

    def __str__(self):
        return self.name

class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    faculty_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    # CRITICAL: This method must exist inside the Faculty class!
    def __str__(self):
        return self.faculty_name

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)

    credits = models.IntegerField(default=3, help_text="Credit hours for this subject")
    full_marks = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)

    def __str__(self):
        return self.subject_name

class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    
    # 2. ForeignKey remains here.
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    enrollment_date = models.DateField(auto_now_add=True)

    # Note: We completely removed the "class Meta: unique_together" block 
    # because OneToOneField automatically makes the student unique!

    def __str__(self):
        return f"{self.student.name} - {self.course.course_name}"

class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=150)
    exam_date = models.DateField()
    semester = models.IntegerField(
        default=1, 
        help_text="Enter the semester number (e.g., 1 for 1st Semester, 2 for 2nd)"
    )

    def __str__(self):
        return f"{self.exam_name} (Semester {self.semester})"

class Result(models.Model):
    result_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2, blank=True)
    grade_point = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = ('student', 'exam')

    def __str__(self):
        return f"{self.student.name} - {self.exam.exam_name}"
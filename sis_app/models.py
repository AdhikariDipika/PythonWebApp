from django.db import models

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

    def __str__(self):
        return f"{self.exam_name} ({self.subject.subject_name})"

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
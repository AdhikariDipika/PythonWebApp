from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Student, Faculty, Subject, Enrollment, Exam, Result
from .forms import CourseForm, StudentForm, FacultyForm, SubjectForm, EnrollmentForm, ExamForm, ResultForm
from .utils import calculate_grade, calculate_grade_point, calculate_gpa

def dashboard(request):
    context = {
        'total_students': Student.objects.count(),
        'total_courses': Course.objects.count(),
        'total_faculty': Faculty.objects.count(),
        'total_subjects': Subject.objects.count(),
        'total_enrollments': Enrollment.objects.count(),
        'total_exams': Exam.objects.count(),
        'total_results': Result.objects.count(),
    }
    return render(request, 'dashboard.html', context)


# ==========================================================================
# 1. STUDENT CRUD
# ==========================================================================
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/form.html', {'form': form, 'title': 'Add Student'})

def student_edit(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/form.html', {'form': form, 'title': 'Edit Student'})

def student_delete(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/delete.html', {'obj': student, 'cancel_url': 'student_list'})


# ==========================================================================
# 2. COURSE CRUD
# ==========================================================================
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})

def course_add(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request, 'courses/form.html', {'form': form, 'title': 'Add Course'})

def course_edit(request, id):
    course = get_object_or_404(Course, pk=id)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request, 'courses/form.html', {'form': form, 'title': 'Edit Course'})

def course_delete(request, id):
    course = get_object_or_404(Course, pk=id)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'courses/delete.html', {'obj': course, 'cancel_url': 'course_list'})


# ==========================================================================
# 3. FACULTY CRUD
# ==========================================================================
def faculty_list(request):
    return render(request, 'faculty/list.html', {'faculty': Faculty.objects.all()})

def faculty_add(request):
    form = FacultyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('faculty_list')
    return render(request, 'faculty/form.html', {'form': form, 'title': 'Add Faculty'})

def faculty_edit(request, id):
    faculty = get_object_or_404(Faculty, pk=id)
    form = FacultyForm(request.POST or None, instance=faculty)
    if form.is_valid():
        form.save()
        return redirect('faculty_list')
    return render(request, 'faculty/form.html', {'form': form, 'title': 'Edit Faculty'})

def faculty_delete(request, id):
    faculty = get_object_or_404(Faculty, pk=id)
    if request.method == 'POST':
        faculty.delete()
        return redirect('faculty_list')
    return render(request, 'faculty/delete.html', {'obj': faculty, 'cancel_url': 'faculty_list'})


# ==========================================================================
# 4. SUBJECT CRUD
# ==========================================================================
def subject_list(request):
    return render(request, 'subjects/list.html', {'subjects': Subject.objects.all()})

def subject_add(request):
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('subject_list')
    return render(request, 'subjects/form.html', {'form': form, 'title': 'Add Subject'})

def subject_edit(request, id):
    subject = get_object_or_404(Subject, pk=id)
    form = SubjectForm(request.POST or None, instance=subject)
    if form.is_valid():
        form.save()
        return redirect('subject_list')
    return render(request, 'subjects/form.html', {'form': form, 'title': 'Edit Subject'})

def subject_delete(request, id):
    subject = get_object_or_404(Subject, pk=id)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'subjects/delete.html', {'obj': subject, 'cancel_url': 'subject_list'})


# ==========================================================================
# 5. ENROLLMENT CRUD
# ==========================================================================
def enrollment_list(request):
    return render(request, 'enrollments/list.html', {'enrollments': Enrollment.objects.all()})

def enrollment_add(request):
    form = EnrollmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('enrollment_list')
    return render(request, 'enrollments/form.html', {'form': form, 'title': 'Add Enrollment'})

def enrollment_edit(request, id):
    enrollment = get_object_or_404(Enrollment, pk=id)
    form = EnrollmentForm(request.POST or None, instance=enrollment)
    if form.is_valid():
        form.save()
        return redirect('enrollment_list')
    return render(request, 'enrollments/form.html', {'form': form, 'title': 'Edit Enrollment'})

def enrollment_delete(request, id):
    enrollment = get_object_or_404(Enrollment, pk=id)
    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollment_list')
    return render(request, 'enrollments/delete.html', {'obj': enrollment, 'cancel_url': 'enrollment_list'})


# ==========================================================================
# 6. EXAM CRUD
# ==========================================================================
def exam_list(request):
    return render(request, 'exams/list.html', {'exams': Exam.objects.all()})

def exam_add(request):
    form = ExamForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('exam_list')
    return render(request, 'exams/form.html', {'form': form, 'title': 'Add Exam'})

def exam_edit(request, id):
    exam = get_object_or_404(Exam, pk=id)
    form = ExamForm(request.POST or None, instance=exam)
    if form.is_valid():
        form.save()
        return redirect('exam_list')
    return render(request, 'exams/form.html', {'form': form, 'title': 'Edit Exam'})

def exam_delete(request, id):
    exam = get_object_or_404(Exam, pk=id)
    if request.method == 'POST':
        exam.delete()
        return redirect('exam_list')
    return render(request, 'exams/delete.html', {'obj': exam, 'cancel_url': 'exam_list'})


# ==========================================================================
# 7. PERFORMANCE LEDGER & TRANSCRIPT LOGIC
# ==========================================================================
def result_list(request):
    # CHANGED: Queries Students instead of raw Result rows to display CGPA aggregates
    students = Student.objects.all()
    return render(request, 'results/list.html', {'students': students})

def student_transcript(request, student_id):
    # 1. Use 'pk' (Primary Key) instead of 'id' to bypass custom column names
    student = get_object_or_404(Student, pk=student_id)
    
    # 2. Query the Result model directly to avoid related_name attribute errors
    detailed_results = Result.objects.filter(student=student).select_related('exam__subject').order_by('exam__semester', 'exam__subject__subject_name')
    
    return render(request, 'results/transcript.html', {
        'student': student,
        'detailed_results': detailed_results
    })

def result_add(request):
    form = ResultForm(request.POST or None)
    if form.is_valid():
        result = form.save(commit=False)
        result.grade = calculate_grade(result.marks)
        result.grade_point = calculate_grade_point(result.marks)
        result.save()
        return redirect('result_list')
    return render(request, 'results/form.html', {'form': form, 'title': 'Add Result'})

def result_edit(request, id):
    result = get_object_or_404(Result, pk=id)
    form = ResultForm(request.POST or None, instance=result)
    if form.is_valid():
        res = form.save(commit=False)
        res.grade = calculate_grade(res.marks)
        res.grade_point = calculate_grade_point(res.marks)
        res.save()
        return redirect('result_list')
    return render(request, 'results/form.html', {'form': form, 'title': 'Edit Result'})

def result_delete(request, id):
    result = get_object_or_404(Result, pk=id)
    if request.method == 'POST':
        result.delete()
        return redirect('result_list')
    return render(request, 'results/delete.html', {'obj': result, 'cancel_url': 'result_list'})


# ==========================================================================
# 8. LEGACY REPORT VIEWS (Optional/Retained)
# ==========================================================================
def student_report(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    enrollments = Enrollment.objects.filter(student=student)
    results = Result.objects.filter(student=student)
    
    report_data = []
    for res in results:
        report_data.append({
            'subject': res.exam.subject.subject_name,
            'exam_name': res.exam.exam_name,
            'marks': res.marks,
            'grade': res.grade,
            'grade_point': res.grade_point,
            'status': 'Pass' if res.marks >= 40 else 'Fail'
        })

    gpa = calculate_gpa(student_id)
    
    context = {
        'student': student,
        'enrollments': enrollments,
        'report_data': report_data,
        'gpa': gpa
    }
    return render(request, 'results/report.html', context)
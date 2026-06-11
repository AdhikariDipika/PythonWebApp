from .models import Result

def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B+'
    elif marks >= 60:
        return 'B'
    elif marks >= 50:
        return 'C+'
    elif marks >= 40:
        return 'C'
    else:
        return 'F'

def calculate_grade_point(marks):
    if marks >= 90:
        return 4.0
    elif marks >= 80:
        return 3.6
    elif marks >= 70:
        return 3.2
    elif marks >= 60:
        return 2.8
    elif marks >= 50:
        return 2.4
    elif marks >= 40:
        return 2.0
    else:
        return 0.0

def calculate_gpa(student_id):
    results = Result.objects.filter(student_id=student_id)
    if not results.exists():
        return 0.0
    
    total_points = sum(result.grade_point for result in results if result.grade_point is not None)
    return round(float(total_points) / results.count(), 2)
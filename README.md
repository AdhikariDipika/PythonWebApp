# Student Information Management System (SIMS)

A simple and maintainable **Django + PostgreSQL** application for managing academic records, including students, courses, subjects, faculty assignments, enrollments, examinations, grading, and performance reporting.

---

## Features

### Dashboard
- Displays real-time summary cards for all major records.
- Quick navigation to management sections.

### Student Management
- Add, view, update, and delete student records.
- Store student details such as name, email, phone number, and address.

### Course & Subject Management
- Manage courses and their associated subjects.
- Maintain course-to-subject relationships.

### Faculty Assignment
- Assign faculty members to specific subjects.
- Track teaching responsibilities.

### Enrollment Management
- Enroll students into courses.
- Prevent duplicate enrollment of the same student in the same course.

### Exam Management
- Schedule and manage examinations.
- Associate exams with subjects.

### Automated Grading
- Automatically calculates grades and grade points when marks are entered or updated.
- Supports pass/fail evaluation.

### Student Performance Reports
- Generate student report cards.
- Display subject-wise marks, grades, pass/fail status, and cumulative GPA.

---

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Configure PostgreSQL

Create a PostgreSQL database and update the database credentials in your Django settings file.

---

### 3. Run Migrations

Create migration files:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

---

### 4. Start the Development Server

```bash
python manage.py runserver
```

---

### 5. Open the Application

Visit:

```text
http://127.0.0.1:8000/
```

The application will load directly into the dashboard where you can manage students, courses, subjects, enrollments, exams, and results.

---

## Main Modules

- Dashboard
- Students
- Courses
- Subjects
- Faculty
- Enrollments
- Exams
- Results & GPA Reports

---

## Built With

- Django
- PostgreSQL
- Python
- HTML/CSS

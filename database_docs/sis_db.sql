-- 1. Create Course Table
CREATE TABLE course (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(200) NOT NULL
);

-- 2. Create Student Table
CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL
);

-- 3. Create Faculty Table
CREATE TABLE faculty (
    faculty_id SERIAL PRIMARY KEY,
    faculty_name VARCHAR(150) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL
);

-- 4. Create Subject Table
CREATE TABLE subject (
    subject_id SERIAL PRIMARY KEY,
    subject_name VARCHAR(200) NOT NULL,
    course_id INT NOT NULL,
    faculty_id INT,
    CONSTRAINT fk_subject_course FOREIGN KEY (course_id) 
        REFERENCES course(course_id) ON DELETE CASCADE,
    CONSTRAINT fk_subject_faculty FOREIGN KEY (faculty_id) 
        REFERENCES faculty(faculty_id) ON DELETE SET NULL
);

-- 5. Create Enrollment Table
CREATE TABLE enrollment (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL UNIQUE,  
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    CONSTRAINT fk_enrollment_student FOREIGN KEY (student_id) 
        REFERENCES student(student_id) ON DELETE CASCADE,
    CONSTRAINT fk_enrollment_course FOREIGN KEY (course_id) 
        REFERENCES course(course_id) ON DELETE CASCADE
);

-- 6. Create Exam Table
CREATE TABLE exam (
    exam_id SERIAL PRIMARY KEY,
    subject_id INT NOT NULL,
    exam_name VARCHAR(150) NOT NULL,
    exam_date DATE NOT NULL,
    CONSTRAINT fk_exam_subject FOREIGN KEY (subject_id) 
        REFERENCES subject(subject_id) ON DELETE CASCADE
);

-- 7. Create Result Table
CREATE TABLE result (
    result_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    exam_id INT NOT NULL,
    marks NUMERIC(5, 2) NOT NULL,
    grade VARCHAR(2) NOT NULL,
    grade_point NUMERIC(3, 2),
    CONSTRAINT fk_result_student FOREIGN KEY (student_id) 
        REFERENCES student(student_id) ON DELETE CASCADE,
    CONSTRAINT fk_result_exam FOREIGN KEY (exam_id) 
        REFERENCES exam(exam_id) ON DELETE CASCADE,
    CONSTRAINT unique_student_exam UNIQUE (student_id, exam_id)
);
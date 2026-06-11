CREATE TABLE "course"(
    "course_id" SERIAL NOT NULL,
    "course_name" VARCHAR(200) NOT NULL
);
ALTER TABLE
    "course" ADD PRIMARY KEY("course_id");
CREATE TABLE "student"(
    "student_id" SERIAL NOT NULL,
    "name" VARCHAR(150) NOT NULL,
    "email" VARCHAR(254) NOT NULL,
    "phone" VARCHAR(20) NOT NULL,
    "address" TEXT NOT NULL
);
ALTER TABLE
    "student" ADD PRIMARY KEY("student_id");
ALTER TABLE
    "student" ADD CONSTRAINT "student_email_unique" UNIQUE("email");
CREATE TABLE "faculty"(
    "faculty_id" SERIAL NOT NULL,
    "faculty_name" VARCHAR(150) NOT NULL,
    "email" VARCHAR(254) NOT NULL,
    "phone" VARCHAR(20) NOT NULL
);
ALTER TABLE
    "faculty" ADD PRIMARY KEY("faculty_id");
ALTER TABLE
    "faculty" ADD CONSTRAINT "faculty_email_unique" UNIQUE("email");
CREATE TABLE "subject"(
    "subject_id" SERIAL NOT NULL,
    "subject_name" VARCHAR(200) NOT NULL,
    "course_id" INTEGER NOT NULL,
    "faculty_id" INTEGER NULL
);
ALTER TABLE
    "subject" ADD PRIMARY KEY("subject_id");
CREATE TABLE "enrollment"(
    "enrollment_id" SERIAL NOT NULL,
    "student_id" INTEGER NOT NULL,
    "course_id" INTEGER NOT NULL,
    "enrollment_date" DATE NOT NULL DEFAULT CURRENT_DATE
);
ALTER TABLE
    "enrollment" ADD CONSTRAINT "enrollment_student_id_course_id_unique" UNIQUE("student_id", "course_id");
ALTER TABLE
    "enrollment" ADD PRIMARY KEY("enrollment_id");
CREATE TABLE "exam"(
    "exam_id" SERIAL NOT NULL,
    "subject_id" INTEGER NOT NULL,
    "exam_name" VARCHAR(150) NOT NULL,
    "exam_date" DATE NOT NULL
);
ALTER TABLE
    "exam" ADD PRIMARY KEY("exam_id");
CREATE TABLE "result"(
    "result_id" SERIAL NOT NULL,
    "student_id" INTEGER NOT NULL,
    "exam_id" INTEGER NOT NULL,
    "marks" DECIMAL(5, 2) NOT NULL,
    "grade" VARCHAR(2) NOT NULL,
    "grade_point" DECIMAL(3, 2) NULL
);
ALTER TABLE
    "result" ADD CONSTRAINT "result_student_id_exam_id_unique" UNIQUE("student_id", "exam_id");
ALTER TABLE
    "result" ADD PRIMARY KEY("result_id");
ALTER TABLE
    "enrollment" ADD CONSTRAINT "enrollment_student_id_foreign" FOREIGN KEY("student_id") REFERENCES "student"("student_id");
ALTER TABLE
    "subject" ADD CONSTRAINT "subject_faculty_id_foreign" FOREIGN KEY("faculty_id") REFERENCES "faculty"("faculty_id");
ALTER TABLE
    "subject" ADD CONSTRAINT "subject_course_id_foreign" FOREIGN KEY("course_id") REFERENCES "course"("course_id");
ALTER TABLE
    "result" ADD CONSTRAINT "result_exam_id_foreign" FOREIGN KEY("exam_id") REFERENCES "exam"("exam_id");
ALTER TABLE
    "enrollment" ADD CONSTRAINT "enrollment_course_id_foreign" FOREIGN KEY("course_id") REFERENCES "course"("course_id");
ALTER TABLE
    "result" ADD CONSTRAINT "result_student_id_foreign" FOREIGN KEY("student_id") REFERENCES "student"("student_id");
ALTER TABLE
    "exam" ADD CONSTRAINT "exam_subject_id_foreign" FOREIGN KEY("subject_id") REFERENCES "subject"("subject_id");
###  Data Dictionary

#### Table: `Course`

| **Column Name** | **Data Type** | **Constraints**             | **Description**                             |
| --------------- | ------------- | --------------------------- | ------------------------------------------- |
| `course_id`     | SERIAL (INT)  | Primary Key, Auto Increment | Unique identifier for each course entity    |
| `course_name`   | VARCHAR(200)  | Not Null                    | The official name designation of the course |

#### Table: `Student`

| **Column Name** | **Data Type** | **Constraints**             | **Description**                                   |
| --------------- | ------------- | --------------------------- | ------------------------------------------------- |
| `student_id`    | SERIAL (INT)  | Primary Key, Auto Increment | Unique identifier for individual student profiles |
| `name`          | VARCHAR(150)  | Not Null                    | Full legal name of the registered student         |
| `email`         | VARCHAR(254)  | Unique, Not Null            | Academic or personal contact email address        |
| `phone`         | VARCHAR(20)   | Not Null                    | Contact phone number string                       |
| `address`       | TEXT          | Not Null                    | Permanent or local residential address mapping    |

#### Table: `Faculty`

| **Column Name** | **Data Type** | **Constraints**             | **Description**                                   |
| --------------- | ------------- | --------------------------- | ------------------------------------------------- |
| `faculty_id`    | SERIAL (INT)  | Primary Key, Auto Increment | Unique tracking identifier for instructor entries |
| `faculty_name`  | VARCHAR(150)  | Not Null                    | Full name of the faculty professor                |
| `email`         | VARCHAR(254)  | Unique, Not Null            | Institutional contact email address               |
| `phone`         | VARCHAR(20)   | Not Null                    | Direct office or personal contact line            |

#### Table: `Subject`

| **Column Name** | **Data Type** | **Constraints**                                          | **Description**                                           |
| --------------- | ------------- | -------------------------------------------------------- | --------------------------------------------------------- |
| `subject_id`    | SERIAL (INT)  | Primary Key, Auto Increment                              | Unique identifier for a curricular subject unit           |
| `subject_name`  | VARCHAR(200)  | Not Null                                                 | The descriptive title of the specific subject module      |
| `course_id`     | INT           | Foreign Key $\rightarrow$ `Course.course_id`             | Link establishing what parent academic course it maps to  |
| `faculty_id`    | INT           | Foreign Key $\rightarrow$ `Faculty.faculty_id`, Nullable | Links the assigned primary faculty handler to the subject |

#### Table: `Enrollment`

| **Column Name**   | **Data Type** | **Constraints**                                | **Description**                                         |
| ----------------- | ------------- | ---------------------------------------------- | ------------------------------------------------------- |
| `enrollment_id`   | SERIAL (INT)  | Primary Key, Auto Increment                    | Unique structural transaction key for each entry record |
| `student_id`      | INT           | Foreign Key $\rightarrow$ `Student.student_id` | The student identity processing the enrollment unit     |
| `course_id`       | INT           | Foreign Key $\rightarrow$ `Course.course_id`   | The course structural tract being registered into       |
| `enrollment_date` | DATE          | Not Null, Auto Now Add                         | Timestamp record when registration took place           |

> **Composite Unique Constraint:** `(student_id, course_id)` prevents duplicating identical student mappings to a single course entry path.

#### Table: `Exam`

| **Column Name** | **Data Type** | **Constraints**                                | **Description**                                             |
| --------------- | ------------- | ---------------------------------------------- | ----------------------------------------------------------- |
| `exam_id`       | SERIAL (INT)  | Primary Key, Auto Increment                    | Unique tracking key for a scheduled examination unit        |
| `subject_id`    | INT           | Foreign Key $\rightarrow$ `Subject.subject_id` | Link validating the parent educational subject evaluated    |
| `exam_name`     | VARCHAR(150)  | Not Null                                       | Named instance definition (e.g., Midterm, Final Assessment) |
| `exam_date`     | DATE          | Not Null                                       | Calendar evaluation delivery date constraint value          |

#### Table: `Result`

| **Column Name** | **Data Type** | **Constraints**                                | **Description**                                              |
| --------------- | ------------- | ---------------------------------------------- | ------------------------------------------------------------ |
| `result_id`     | SERIAL (INT)  | Primary Key, Auto Increment                    | Unique row sequence indexing key for results data sheets     |
| `student_id`    | INT           | Foreign Key $\rightarrow$ `Student.student_id` | The target student receiving the graded scorecard mapping    |
| `exam_id`       | INT           | Foreign Key $\rightarrow$ `Exam.exam_id`       | The exact assessment context being indexed                   |
| `marks`         | NUMERIC(5,2)  | Not Null                                       | Numerical grade raw marks received ($0.00 \le \text{marks} \le 100.00$) |
| `grade`         | VARCHAR(2)    | Blank Allowed (Computed)                       | Alpha grade assignment character key (e.g., A+, B, F)        |
| `grade_point`   | NUMERIC(3,2)  | Blank/Null Allowed (Computed)                  | Standard internal quality grade point value weight assignment |

> 
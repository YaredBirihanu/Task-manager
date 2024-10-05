class Institution:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        return f"{self.name}, located at {self.location}"

class Student:
    def __init__(self, student_id, name):
        self._student_id = student_id
        self._name = name
        self._enrolled_courses = []
        self._grades = {}
        self._attendance = {}

    def enroll(self, course):
        self._enrolled_courses.append(course)
        course.add_student(self)

    def add_grade(self, course, grade):
        self._grades[course] = grade

    def get_average(self):
        if not self._grades:
            return 0
        return sum(self._grades.values()) / len(self._grades)

    def get_info(self):
        return f"ID: {self._student_id}, Name: {self._name}, Enrolled Courses: {len(self._enrolled_courses)}"

    def mark_attendance(self, course, date, present=True):
        if course not in self._attendance:
            self._attendance[course] = {}
        self._attendance[course][date] = present

    def check_attendance(self, course):
        return self._attendance.get(course, {})

class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_student_list(self):
        return [student.get_info() for student in self.students]

class School(Institution):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.courses = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def list_courses(self):
        return [course.course_name for course in self.courses]

    def add_student(self, student):
        self.students.append(student)

    def search_student(self, search_term):
        result = []
        for student in self.students:
            if search_term in student._name or search_term == student._student_id:
                result.append(student.get_info())
        return result

# Example usage
school = School("ABC Academy", "New York")
course1 = Course("CS101", "Introduction to Computer Science")
course2 = Course("MATH101", "Calculus I")

school.add_course(course1)
school.add_course(course2)

student1 = Student("001", "Alice")
student1.enroll(course1)
student1.add_grade(course1, 90)
school.add_student(student1)

student2 = Student("002", "Bob")
student2.enroll(course2)
student2.add_grade(course2, 85)
school.add_student(student2)

# Mark attendance
student1.mark_attendance(course1, "2024-10-01", present=True)
student1.mark_attendance(course1, "2024-10-02", present=False)
student2.mark_attendance(course2, "2024-10-01", present=True)

# Searching for students
print(school.search_student("Alice"))  # Search by name
print(school.search_student("002"))     # Search by ID

# Check attendance
print(f"Attendance for {student1._name} in {course1.course_name}: {student1.check_attendance(course1)}")
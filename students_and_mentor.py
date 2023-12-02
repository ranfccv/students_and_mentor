
class Student:
    def __init__(self, name, surname, gender):
        self.courses_attached = []
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def str(self):
        return f"Student(name={self.name},surname={self.surname},ever_grade={self.ever_grade()},courses_in_progress={self.courses_in_progress},finished_courses{self.finished_courses}"


class Lecturer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def str(self):
        return f"Student(name={self.name},surname={self.surname},ever_grade={self.ever_grade()}"
class Reviewer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def str(self):
        return f"Student(name={self.name},surname={self.surname}"


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor(Lecturer, Reviewer):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)
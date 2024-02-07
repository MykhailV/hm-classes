def _avg_grade(self):
    sum_ = 0
    marks_count = 0
    for value in self.grades.values():
        sum_ += sum(value)
        marks_count += len(value)
    if sum_ != 0 and marks_count != 0:
        mid = sum_ / marks_count
        return round(mid, 1)
    else:
        return 0


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {_avg_grade(self)}\nКурсы в процессе изучения:"
                f" {', '.join(self.courses_in_progress)}\nЗавершенные курсы: Введение в программирование")

    def __lt__(self, other):
        return _avg_grade(self) < _avg_grade(other)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {_avg_grade(self)}"


    def __lt__(self, other):
        return _avg_grade(self) < _avg_grade(other)


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def avg_grade(students, course_):
    sum_ = 0
    marks_count = 0
    for student in students:
        if course_ in student.grades:
            sum_ += sum(student.grades.get(course_))
            marks_count += len(student.grades.get(course_))
    if sum_ != 0 and marks_count != 0:
        mid = sum_ / marks_count
        return round(mid, 1)
    else:
        return 0


def avg_grade2(lectors, course_):
    sum_ = 0
    marks_count = 0
    for lector in lectors:
        if course_ in lector.grades:
            sum_ += sum(lector.grades.get(course_))
            marks_count += len(lector.grades.get(course_))
    if sum_ != 0 and marks_count != 0:
        mid = sum_ / marks_count
        return round(mid, 1)
    else:
        return 0



best_student = Student('Ruoy', 'Eman', 'your_gender')
bad_student = Student('Sam', 'Johnson', 'male')

best_student.courses_in_progress += ['Python', 'Git']
bad_student.courses_in_progress += ['Python', 'Git']

cool_reviewer = Reviewer('Some', 'Buddy')
norm_reviewer = Reviewer('Ken', 'Daddy')

cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer1 = Lecturer('Garry', 'Osley')
cool_lecturer1.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer1, 'Python', 7)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(bad_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)

print(cool_reviewer)
# print(norm_reviewer)

# print(cool_lecturer)
print(cool_lecturer1)

print(best_student)

print(cool_lecturer > cool_lecturer1)
print(best_student > bad_student)

print(_avg_grade(cool_lecturer))
print(_avg_grade(best_student))

print(avg_grade([best_student, bad_student], 'Python'))
print(avg_grade2([cool_lecturer, cool_lecturer1], 'Python'))

# print(best_student.grades)

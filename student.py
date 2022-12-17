class Human:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender

    def __str__(self):
        card = f'Имя: {self.name} \n' \
                f'Фамилия: {self.surname}'
        return card

    def __lt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student) or isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        elif isinstance(other, Reviewer) or isinstance(self, Reviewer):
            return 'Ревьюеры несравненны )'
        else:
            return 'Разные классы объектов не сравнимы.'

    def average_grade(self):
        if isinstance(self, Reviewer):
            return 'Ревьюеры не получают оценок.'
        else:
            summ = round(sum(*self.grades.values()) / len(*self.grades.values()), 1)
            return summ


class Student(Human):
    def __init__(self, name, surname, gender):
        super(). __init__(name, surname, gender)
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        student_card = f'{super().__str__()} \n' \
                        f'Средняя оценка за домашние задания: {super().average_grade()} \n' \
                        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
                        f'Завершенные курсы: {", ".join(self.finished_courses)} \n------------'
        return student_card

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor(Human):
    def __init__(self, name, surname, gender):
        super(). __init__(name, surname, gender)
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __str__(self):
        lecturer_card = f'{super().__str__()} \n' \
                        f'Средняя оценка за лекции: {super().average_grade()} \n------------'
        return lecturer_card

    def __init__(self, name, surname, gender):
        super(). __init__(name, surname, gender)
        self.grades = {}


def average_rate_stud(*stud, course):
    summ = 0
    count = 0
    for student in stud:
        summ += sum(student.grades[course])
        count += len(student.grades[course])
    return round(summ / count, 1)

def average_rate_lect(*lect, course):
    summ = 0
    count = 0
    for lecturer in lect:
        summ += sum(lecturer.grades[course])
        count += len(lecturer.grades[course])
    return round(summ / count, 1)

best_student = Student('Иван', 'Петров', 'муж')
best_student.courses_in_progress += ['Си', 'Java', 'Python']
best_student.finished_courses += ['Go']

other_student = Student('Елена', 'Сидорова', 'жен')
other_student.courses_in_progress += ['Python', 'Go']
other_student.finished_courses += ['Java']

best_lecturer = Lecturer('Игорь', 'Иванов', 'муж')
best_lecturer.courses_attached += ['Python', 'Java']

other_lecturer = Lecturer('Татьяна', 'Панова', 'жен')
other_lecturer.courses_attached += ['Си', 'Go', 'Python']

best_student.rate_hw(best_lecturer, 'Python', 10)
best_student.rate_hw(best_lecturer, 'Python', 7)
best_student.rate_hw(best_lecturer, 'Python', 9)

other_student.rate_hw(other_lecturer, 'Python', 9)
other_student.rate_hw(other_lecturer, 'Python', 10)
other_student.rate_hw(other_lecturer, 'Python', 10)

cool_reviewer = Reviewer('Пётр', 'Балашов', 'муж')
cool_reviewer.courses_attached += ['Python', 'Pascal', 'Go', 'Java', 'Си']

cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 6)

cool_reviewer.rate_hw(other_student, 'Python', 10)
cool_reviewer.rate_hw(other_student, 'Python', 8)
cool_reviewer.rate_hw(other_student, 'Python', 10)

print(best_student < cool_reviewer)
print(best_student < other_lecturer)
print(best_student > other_student)
print(best_student)
print(other_student)
print(best_lecturer)
print(cool_reviewer)
print(average_rate_stud(best_student, other_student, course='Python'))
print(average_rate_lect(best_lecturer, other_lecturer, course='Python'))
class Student:
    def __init__(self, name, age, hobbie):
        self.name = name
        self.age = age
        self.hobbie = hobbie
        self.rank = 'двоечник'
class Group:
    def __init__(self, name):
        self.name = name
        self.students = []
    def addNewStudent(self, student):
        self.students.append(student)
        print(student.name + ' added to group ' + self.name + '!')
    def printAllStudents(self):
        print('Список студентов группы ' + group.name + ':')
        for student in self.students:
            print(student.name)
    def printAllStudentsHobbie(self):
        for student in self.students:
            print(student.name + ' увлекается ', end='')
            print(student.hobbies)
    def printAllStudentWhoLikeThisHobbie(self, hobbie):
        # TODO: создать функцию которая выводит на экран всех учеников с определенным хобби
        pass
    def printAllStudentWhoOlderThan16(self):
        # TODO: создать функцию которая выводит на экран всех учеников старше 16
        pass
    def rankSet(self):
        # TODO: создать функцию проставляющую всем ученикам в группе оценку
        pass
import random
rank = ['двоечник', 'троечник', 'хорошист' , 'отличник', 'сын маминой подруги']
names = ['Кугунуров Андрей','Рожков Денис','Санников Никита', 'Бысыев Дьулустаан', 'Соловьев Артем']
hobbies = ['компьютерные игры', 'кубик-кубика', 'футбол', 'баскетбол', 'тетрис', 'настольный теннис']
group = Group('МИТ-10')
# TODO: сделать нормальную генерацию группы (добавить имена и чтоб в группу двух с одинаковыми именами не добавляло
for i in range(10):
    group.addNewStudent(Student(random.choice(names), random.randint(14,18), random.choice(hobbies)))
group.printAllStudents()
#group.printAllStudentsHobbie()

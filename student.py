class Student:
    def __init__(self, name, age, group, hobbies):
        self.name = name
        self.age = age
        self.group = group
        self.hobbies = hobbies
    def getAllHobbies(self):
        for hobbie in self.hobbies:
            return(hobbie)
class Group:
    def __init__(self, name):
        self.name = name
        self.students = []
    def addNewStudent(self, student):
        self.students.append(student)
        print(student.name + ' added to group ' + self.name + '!')
    def printAllStudents(self):
        for student in self.students:
            print(student.name)

group1 = Group('МИТ-10')
student1 = Student('Кугунуров Андрей', 16, group1, ['компьютерные игры', 'кубик-кубика'])
group1.addNewStudent(student1)
print('Список студентов группы ' + group1.name + ':')
group1.printAllStudents()
for student in group1.students:
    print(student.name + ' увлекается ', end='')
    print(student.hobbies)

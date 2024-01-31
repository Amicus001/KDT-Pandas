
class Person4:
    def greeting(self):
        print("hi!")
class Student(Person4):
    def study(self):
        print('study')
james = Student()
james.greeting()
james.study()

print('--------------------상속 관계-------------------------')
class Person4:
    def greeting(self):
        print("hi!")
class personlist:
    def __init__(self):
        self.person_list = []
    def append_person(self,person):
        self.person_list.append(person)

print('-------------------------기반 클래스의 속성 사용하기--------------------------')
class Person4:
    def greeting(self):
        print("hi!")
class Student(Person4):
    def study(self):
        self.school = 'python school'

print('----------------------------super()로 기반 클래스 초기화하기----------------------')

class Person5:
    def __init__(self):
        print('person __init__')
        self.hello = 'hi!'

class Student2(Person5):
    def __init__(self):
        print ('Studint __init__')
        self.school = 'python'

james = Student2()
print(james.school)
print(james.hello)

print('------------------------------기반 클래스를 초기화하지 않는 경우--------------------------------')
class Person:
    def __init__(self):
        print ('Person__init__')
        self.hello = 'hi!'

class Student(Person):
    pass

james = Student()

print('-------------메서드 오버라이딩 사용하기------------------------')

class Person:
    def greeting(self):
        print('hi!')

class student:
    def greetings(self):
        super().greeting()
        print(', i am a student.')

james = student()
james.greeting()


#예제 풀어보기
class Person:
    bag = []

    def put_bag(self, stuff):
        Person.bag.append(stuff) #클래스 이름으로 속성에 접근하기.
    #    self.bag.append(stuff)


james = Person()
james.put_bag('book')

maria = Person()
maria.put_bag('key')
print('-----------------클래스 만들기------------------------')
print(james.bag)
print(maria.bag)
print(Person.bag)
print('-----------------인스턴스 속성 사용하기-----------------')
#===========================================================
#인스턴스 속성 사용하기

class Person2:
    def __init__(self):
        self.bag = []
    def put_bag(self,stuff):
        self.bag.append(stuff)

james = Person2()
james.put_bag('book')

maria = Person2()
maria.put_bag('key')

print(james.bag)
print(maria.bag)
print('----------------비공개 클래스 속성 사용하기------------------------')

#class classname:
#      __속성 = 값 <-클래스 안에서만 접근 가능

class Knight:
    __item_limit = 10 #비공개 클래스 속성

    def print_item_limit(self):
        print(Knight.__item_limit) #클래스 내부에서만 접근이 됨

x = Knight()
#x.print_item_limit(): 접근 불가
print(Knight.print_item_limit) #클래스 밖에서는 접근 불가
print('--------------정적 메서드 사용하기-----------------')

# 정적 메서드 사용하기
class Calc:
    @staticmethod #데코레이터, 메서드에 추가 기능 구현.
    def add(a,b):
        print(a+b)
    @staticmethod
    def mul(a,b):
        print(a*b)
Calc.add(10,20) #클래스에서 바로 메서드 호출하기
Calc.mul(10,20)

print('---------------클래스 메서드 사용하기---------------------')
class Person3:
    count = 0 #클래스 속성: 아무 값도 지정하지 않으면 자동으로 등호 뒤의 항목이 입력된다.
    def __init__(self):
        Person3.count+= 1 #인스턴스가 만들어질 때 클래스 속성 count에 1을 더합니다.

    @classmethod
    def print_count(cls):
        print(f'{0}명 생성되었습니다.'.format(cls.count)) #cls로 클래스 속성에 접근합니다.

james = Person3()
maria = Person3()
Person3.print_count()

print('----------------------------35장 연습문제-----------------------------')
class Date:
    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int,date_string.split('-'))
        return month<= 12 and day<=31
if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 형식입니다.')

print('-------------------35장 심사문제---------------------------------------')

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    @staticmethod

    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string)
        return minute<=60 and second<=60
    @staticmethod
    def from_string(time_string):
        time_string
time_string = input()
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 입력입니다.')



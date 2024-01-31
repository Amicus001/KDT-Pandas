#자동차 클래스
#클래스 이름: car
#속성: 바퀴, 색상, 등록번호, 차종,(= 인스턴스 속성), 제조사(=클래스 속성)
#     12인치 빨강, 1111,  세단, 현대
#       "    "     "      "   "
#기능: 주행, 정지, 후진
#=================================================

class Car:
    #클래스 속성
    brand='Hyundai'

    #생성자 메서드: 객체(인스턴스) 생성 메서드
    def __init__(self, wheel, color, number, kind):
        #heap 영역에 저장
        self.wheel = wheel
        self.color = color
        self.number = number
        self. kind = kind

    #객체(카 인스턴스) 메서드
    def driving(self, destination):
        print(f'{destination}에 {self.number} 차가 주행중')
    def stop(self,parking):
        print(f'{self.number} 차가 {parking}에 정차중')
    def back(self, to):
        print(f'{self.number} 차가 {to}로 후진중')
#자동차 인스턴스 생성
Mycar = Car(19, 'red', 1111,'세단')
second = Car(19, 'purlpe', 7777, 'SUV')

#사랑 클래스
#클래스 이름: love
#속성: kind (one-sided, platonic, agape, etc...),
#기능: 새우 까 주기. 깻잎 떼 주기. 금융치료하기. 데려다 주기. 데이트하기. 같이 아프기. 같이 죽기. 대신 죽어주기.
#     희생하기.
#=================================================
# class Love:
#      def __init__(self,peeling_shrimp, perilla_leaf, showmethemoney, takinghome,
#                   goingout, dyingtogether, sacrifice):
#          def self.perilla_leaf = perilla_leaf
#              print()
#          def self.peeling_shrimp = peeling_shrimp
#              print("새우를 까드리겠습니다.")

#계산기 클래스
#클래스 이름: calc
#속성: 브랜드, 종류, 크기, 색상, 가격, 데이터
#기능: 덧셈. 뺄셈. 곱셈. 나눗셈
#데이터: 속성 또는 기능에서 매개변수로 받을 수 있음

# class calc:
#     #클래스 변수
#     brand = 'Cassio'
#     __size =(7,15)#클래스 밖에서 속성을 읽거나 쓸 수 없음: __속성명
#     #객체(인스턴스) 생성
#     def __init__(self, kind, color, price, info):
#         self.kind = kind
#         self.color = color
#         self.price = price
#         self.data = 0
#         self.__info = info #인스턴스 생성 시 계산기에 각인되는 정보
#     #인스턴스 비공개 속성 읽기/쓰기 전용 메서드 getter/setter
#     @property
#     def info(self):
#         return self.__info
#     def getInfo(self):
#         return self.__info
#
#     def setInfo(self, info):
#         self.__info = info
#     #덧셈 기능
#     def plus(self,nums):
#         self.data += nums
#     def minus(self,nums):
#         self.data-= nums
#     def multiply(self, nums):
#         self.data *=nums
#     def divide(self,nums):
#             if not nums:
#                 return '0으로 나눌 수 없습니다'
#                 self.data = self.data/nums
#     def result(self):
#         return self.data
#     def clear(self):
#         pass
#
# #calc 클래스로 인스턴스 힙에 생성->
# #               인스턴스+클래스 변수 확인하기 가능, 인스턴스 메서드 사용 가능
# c1 = calc('공학용', '검정',30000, '10*20', 'NAME')
# #인스턴스 속성 읽기(공개속성만 읽기가 가능함)
# print(c1)
# #인스턴스 속성 변경(공개속성만 읽기가 가능함)
# c1.color = 'red'
# #인스턴스 비공개 속성 읽기/쓰기 전용 메서드 getter/setter: 속성 읽기/쓰기 방식으로 동작하도록 설정함.
# # 읽기
# print(c1.getInfo(), c1.info)
# #쓰기
# c1.setInfo('MINE')
# #calc 클래스로 계산기 정보 확인: 클래스 변수만 확인 가능, 인스턴스 변수/메서드 사용 불가능
# print(calc.brand)
# #
# #인스턴스 메서드에 접근 불가: print(calc.plus(10,2))
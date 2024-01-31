# #------------------------------------------
# # 자동차 관리 프로그램 만들기
# # 엔진, 연료, 브랜드, 색상, 번호
# # 전진, 후진, 좌회전, 우회전, 정지, etc.
# # -----------------------------------------
#
# engine = '휘발유 엔진'
# food = '휘발유'
# brand = "Hyundai"
# color = "white"
# number = '112가2234'
#
# def go():
#     print("forward")
#
# def back(): print(f"{number}go back")
# def left(): print(f"{number}take a left turn")
# def right(): print(f"{number}Take a right turn")
# def stop(): print(f"{number}Stop")
# cardict = { '111가1111': {'engine': '휘발유', 'co;or':'white', 'brand': 'hyundai'} }
# #관리
# for k, v in cardict.items():
#     print(f'first selling car{k}')
#     for subk, subv in v.items:
#         print(f'{subk}:{subv}')

#자동차 class
#역할  : 자동차 관련 데이터와 기능 모두 저장/관리함
#문법  :
#   class classname:
#   >>>> code

class car:

    #class 생성 시 필수로 사용되는 메서드
    #heap 메모리에 속성들의 값 저장하는 역할
    def __init__(self, engine, brand1, food1, color1, number1):
        print('__init__')
        #자동차 클래스가 가지는 속성을 heap 메모리에 저장
        self.engine= engine
        self.brand= brand1
        self.food= food1
        self.color = color1
        self.number = number1

    #자동차 기능: 함수 형식

    def carfunction(self):
        print(f'{self.number} 차 전진')
    def goingback(self):
        print(f'{self.number}차 후진')
    def stopping(self):
        print(f'{self.number}차 정지')


#클래스로 자동차 객체 생성
mycar = car('휘발유','현대','휘발유','흰색','111가1111')
mucar2 = car('diesel','hyundai','oil','pink','111가1112')
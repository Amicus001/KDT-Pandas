#자율주행자동차 클래스 생성: 상속적용하기
#자율비행자동차 클래스 생성: 상속적용하기
import ex_class_02 as e2

class autodriving(e2.Car):
    def __init__(self, wheel, color, number, kind, autodrive, autofly):
        super().__init__(wheel, color, number, kind)
        self.autodrive = autodrive
        self.autofly = autofly
    #객체(인스턴스) 메서드
    def driving(self, destination):
        print(f'{self.number}차량이 주행을 시작합니다.')
    def stop(self,parking):
        print(f'{self.number}차량이 주행을 멈춥니다.')
    def autodrive(self):
        if self.autodrive() == True:
            print(f'{self.number}차량이 자율주행을 시작합니다.')
    def autofly(self):
        if self.autofly() == True :
            print(f'{self.number}차량이 자율비행을 시작합니다.')

    def printinfo(self):
        print(f'차량번호 {self.number}, {self.wheel}인치 휠, {self.kind}, '
              f'{self.autofly},{self.autodrive}')
#차량 객체 인스턴스 생성하기
bigcar = autodriving(12, 'lavender',5555,'세단',True, False)
bigcar.printinfo()
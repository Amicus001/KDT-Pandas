#2차원 점클래스
#클래스이름: pint2D
#속성: x, y, color, shape, size
#기능: 그리기, 지우기, 정보 출력
#------------------------------------------------------
class pint2D:
    #클래스 속성 없음
    #인스턴스(객체) 생성
    def __init__(self,x, y, color, shape, size):
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.size = size

    def draw(self):
        print(f'좌표: {self.x}, {self.y}에 {self.shape}그리기')

    def printinfo(self):
        print(f'위치: {self.x}, {self.y}')
        print(f'색상 :{self.color}')
        print(f'형태 : {self.shape}')

#3차원 점클래스
#클래스이름: pint2D
#속성: x, y, color, shape, size
#기능: 그리기, 지우기, 정보 출력
#------------------------------------------------------
import ex_class_02 as e2
class pint3D(pint2D,e2.Car): #괄호 안의 클래스= 부모 클래스, 'super'
                      #괄호 밖의 클래스 =자식 클래스, 'sub', 부모클래스에게 없는 인수만 추가함.
    def __init__(self, x,y,z, color, shape, size):
        print('point3d')
        # 상속받은 부모의 메서드를 나의 취향에 맞게 수정하기(오버라이딩)
        super().__init__(x,y,color, shape, size) #부모 객체 생성하기
        self.z = z

    def printinfo(self):
        print('3D')
        print(f'위치: {self.x}, {self.y}, {self.z}')
p2 = pint2D(10, 10, 'red', 'circle', (10,10))
p3 = pint3D(5,5,5, 'yellow', 'rectangle', (3,3,3))
p3.printinfo()

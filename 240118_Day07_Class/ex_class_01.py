#---------------------------------------------------------------------
#사용자 정의 클래스
#---------------------------------------------------------------------
#클래스 정의: 밤하늘의 별을 저장하는 데이터
#클래스 이름: Star
#클래스 속성: 크기, 색상, 밝기; 속성(attribute). 필드(field)-> 변수
#클래스 기능: 반짝거린다. 떨어진다.  -> 함수(function),  메서드(method) -> 함수
#-----------------------------------------------------------------------
# #def __어쩌구__
    #나의 클래스에 맞도록 수정(리모델링)하여 사용하기 = 오버라이드(override)
class Star:
    #클래스 변수/속성/필드: 해당 클래스 생성된 객체(인스턴스)가 공유하는 속성
    timezone = '밤'
    __privateValue = 77
    def __init__(self,size, color, brightness, name = '알 수 없음',):
        print(f'__init__(): {size}, {color}, {brightness}, {name}')#최상위 부모클래스 상속받은 함수(=메서드)
        self.__size = size
        self.color=color
        self.brightness = brightness #힙 영역에 저장: 속성 데이터의 주소 저장

        self.name = name
        # 별 클래스의 기능: 메서드
    def drop(self):
        print(f'{self.name}별이 하늘에서 떨어집니다. 소원 빌어')
        print(f'{self.color}별이 하늘에서 떨어집니다. 소원 빌어')
    #비공개 인스턴스 속성에 접근하기 위한 메서드: getter/setter
    #속성을 읽어 오는 메서드: get(속성명)->속성값 반환
    #비공개 인스턴스 속성에 값을 설정하는 메서드->set속성명(새로운 값)
    def getSize(self):
        return self.__size

    def setsize(self, size):
        self.__size = size
    #비공개 인스턴스 메서드: 클래스 내부에서만 호출되는 메서드
    def __inner(self):
        print("나는 비공개 인스턴스 메서드~")

    #객체(인스턴스) 생성 없이 사용하는 메서드
    @staticmethod
    def add():
        pass

class love:
    @staticmethod
    def smile(self):
        pass
    def cc(cls):
Mystar = Star(5, 'blue', 10)
Yourstar = Star(10, 'red', 20, 'Red star')
#객체 생성: 클래스에 정의된 속성(변수)과 함수들이 메모리의 heap영역에 생성됨
# 생성 방법: 클래스명()<- 생성자 함수
#           클래스명(매개변수1) 생성자 함수/메서드
#           클래스명(매개변수1, 매개변수2, 매개변수3, ..., 매개변수N) 생성자 함수/메서드

# 객체 메서드 실행: 객체변수명.메서드명()
Mystar.drop()
Yourstar.drop()
#객체 속성 읽기; 객체변수명.속성명
# 인스턴스 속성에 직접 접근하기
print(Mystar.brightness, Mystar.timezone, Star.timezone)
print(Yourstar.brightness,Yourstar.timezone, Star.timezone)

# 인스턴스 속성에 간접 접근하기-> 메서드 제공 필수.
print(Mystar.getSize()) #비공개속성앖 읽기
Mystar.setsize(100)# 비공개 속성 값 변경하기
print(Mystar.getSize())
#객체 속성 변경: 개체변수명.속성명=새로운 값
print(f'클래스명.__dict__ :\n{Star.__dict__}')
print(f'인스턴스명.__dict__:\n {Mystar.__dict__}')

#별 클래스의 기능: 메서드

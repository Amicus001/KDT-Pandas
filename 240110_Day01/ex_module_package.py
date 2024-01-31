#---------------------------------------------
# 모듈과 패키지
# 관계; 모듈 - 특정 기능(목적)의 변수, 함수, 클래스를 저장한 하나의 파이썬 파일 .py
#      패키지 - 특정 기능(목적)의 모듈을 담고 있는 단위
#      문법 - import 모듈명
#            import packagename.modulename
#---------------------------------------------
#사용할 모듈 로딩

import math     #내장 모듈 math 내의 모든 변수, 함수, 클래스 다 쓸게~
import math as m #모듈명에 별칭(별명)지정
from math import factorial  #모듈 내에서 factorial 함수만 사용
from math import factorial as fac #모듈 내에서 factorial 함수만 별명 지정하여 사용

#사용자 정의 함수
def factorial(x):
    print (f'{x}!')

#모듈내의 요소(변수, 함수,클래스) 사용법
print(math.pi, math.pow(2,3))
print(m.pi, m.pow(5,9))
#모듈 내의 함수 한 개만 직접 import한 경우 모듈 호출 없이 바로 사용이 가능
print(factorial(5))  #이미 존재하는 함수와 같은 이름으로 사용자 정의 함수를 만들었을 경우 해당 파일 안에서만 덮어쓰기
print(fac(10))
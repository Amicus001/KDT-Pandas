#pandas 패키지설치 확인 및 버전체크
#-----------------------------------

import pandas as pd

print(pd.__version__)

#------------------------
#데이터파일 읽기
#상대 경로: 현재파일을 기준으로 잡아 경로를 설정함
filename = '../DATA/used_cars.csv'

data = pd.read_csv(filename)
print(type(data))
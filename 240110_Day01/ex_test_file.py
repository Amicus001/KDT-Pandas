#---------------------------------
# 입력받은 내용을 파일에 저장하는 프로그램
# 조건: X, x 입력시 입력 받기 중단
# --------------------------------
from datetime import date, datetime
today = date.today()
print(today.year, today.month,today.day)
today2 = datetime.today()
print(today2.year, today2.month, today2.day, today2. hour, today2.minute, today2.second)
#모듈 로딩---------------------------
# import time
# #related variables:
# filename = 'test.txt'
# print(time.time())
# print(time.ctime(time.time()))
# #function
# with open(filename, mode='a', encoding='utf8')as f:
#     while True:
#         data = input("message(press X or x to quit):")
#         # 종료 검사 구문
#         if data in ('X', 'x'):
#             print("Quit")
#             #종료 전에 파일에 기록
#
#             break  # 즉시 종료: while문 안의 아래 코드 실행 안됨
#     f.write(data+'\n')
#
#     #일정시간 일시정지 후 반복
#     time.sleep(1)
#
#     #종료시간 파일에 기록
#     f.write(f'saving time: {time.ctime(time.time())}\n')
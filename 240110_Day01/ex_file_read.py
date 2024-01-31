#------------------------------------------------
# 파일 입츨력/ 출력(읽기)
#  -사용 내장 함수: open(file, mode = 'rt(기본값)', encoding = '시스템기본값')
#  -encoding 설정: 파일에 적용된 인코딩 설정
# -----------------------------------------------
# 1: open
file = open('msg.txt', encoding='utf8')
print(f'file type: {type(file)}')

# # 2: IO =read() : 파일 안의 모든 내용 다 읽어옴
filedata = file.read()
# print(f'filedata ={type(filedata)},{filedata}')

#IO-> read(n):
# filedata = file.read(5) #괄호 안에 지정된 숫자의 갯수만큼 문자를 읽어옴(공백도 문자이므로 공백 포함)
# print(f'filedata ={type(filedata)},{filedata}')
# print(f'filedata ={type(filedata)},{filedata}')

#ID ->readline() # \n 기준으로 한 줄만 읽어오기
data=[]
# while True:
#     fileline = file.readline()
#     if not fileline: break
#     print(f'filedata ={fileline}')
#     datas.append(fileline)

#ID-> readlines(): \n기준으로 한 줄만 읽어오기
datas = file.readlines()
print(datas)
# 3: close
file.close()
#---------------------------------------------
# 입출력 코드 작성시 권장 문법
# open()/close() 가 함께 동작gksms IO의 경우 권장
# 파일 입출력, 데이터베이스 등
# 문법: with open() as 별칭:
# close를 알아서 처리해줌
# --------------------------------------------

filename = 'fruits.txt'

with open(filename, mode='w', encoding= 'utf-8')as f:
    f.write("apple\n")
    f.write("banana\n")
    f.write('pear\n')

with open(filename, mode='r', encoding='utf-8') as f:
    f.write('졸리군.......')
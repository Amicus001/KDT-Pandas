#------------------------------------------------------------
# 파일 데이터 접근 관련 메서드
# -----------------------------------------------------------

filename = 'msg.txt'
with open(filename,mode='r',)as f:
    f.seek(5)
    print(f.read(10))
    print(f'현위치: {f.tell()}')
    f.seek(0)
    print(f'location: {f.tell}')
    print(f.read(5))

print(f.name, f.closed)
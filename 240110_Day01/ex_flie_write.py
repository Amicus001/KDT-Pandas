#-------------------------------------
# 사용 내장 함수: open(file, modw='w', encoding='지정'
# ------------------------------------

filename = 'mydata.txt'
existfile = 'msgk.txt'
#1. open: 쓰기(w)모드의 경우 파일이 없으면 생성함. 있으면 모든 내용 지움.
# file = open(filename,mode='w', encoding='utf-8')
# 1. open: 쓰기(a)모드: 파일이 없으면 생성, 있으면 제일 마지막에 추가
file = open(filename,mode = 'a', encoding='utf-8')

#2 write
file.write("1234567\n")
file.write("f u")
file.writelines(['a','b','c','d','e','f','1112233'])
#3 close
file.close()
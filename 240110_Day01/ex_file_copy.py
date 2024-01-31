#파일을 하나 선택하여 복사본 파일 생성
# ex ) message.txt ======> message_copy.txt

filename = "msg.txt"

#원본파일 읽어와서 저장
with open(filename, mode='r', encoding='utf8')as f:
    data = f.read()
#복사본 파일에 내용 저장
with open('msg_copy.txt', mode='w', encoding='utf8') as f:
    f.write(data)
#원본파일 읽어와서 복사본 파일 저장
with open(filename, mode='r', encoding='utf8')as of:
    with open('msg_copy.txt', mode='w', encoding='utf8') as nf:
        nf.write(of.read())

while True:

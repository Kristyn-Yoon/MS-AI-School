from turtle import *
color('green','blue')
begin_fill()
while True:
    forward(200)
    right(90)
    if abs(pos()) < 1:
        break
end_fill()
done()


#저장하고 터미널로 python .\파일이름
# 파일이름 치다가 tab 키 누르면 저절로 나옴.
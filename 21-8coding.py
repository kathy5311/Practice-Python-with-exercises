import turtle as t 

n,line = map(int, input("숫자를 입력하세요.").split())
t.shape('turtle')
t.speed('fastest')
for i in range(n):
    t.forward(line)
    t.right((360/n)*2)
    t.forward(line)
    t.left(360/n)
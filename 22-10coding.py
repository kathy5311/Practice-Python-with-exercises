a= int(input("숫자를 입력하세요."))
b= int(input("숫자를 입력하세요."))

if a<b:
    c= [2**i for i in range(a,b+1)]
    del c[1]
    del c[-2]
    print(c)

else:
    print("잘못된 숫자 입력")
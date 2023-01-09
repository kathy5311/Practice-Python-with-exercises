a= int(input("write your korean score.: "))
b= int(input("write your english score.: "))
c= int(input("write your math score.: "))
d= int(input("write your science score.: "))

if 0<=a and b and c and d<=100:
    if (a+b+c+d)/4>=80:
        print("합격")
    
    else:
        print('불합격')

else:
    print("잘못된 점수")
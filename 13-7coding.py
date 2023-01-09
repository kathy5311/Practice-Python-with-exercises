a= int(input("write price: "))
b= input("write the coupon's type: ")

if b=='Cash3000':
    print(a-3000)

elif b=='Cash5000':
    print(a-5000)

else:
    print("해당 없음")
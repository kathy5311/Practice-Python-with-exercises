age = int(input("나이를 입력하세요!"))
balance =9000

if age>=7:
    if 7<=age<=12:
        balance=balance-650
    
    elif 13<=age<=18:
        balance= balance-1050
    
    else:
        balance=balance-1250

else:
    balance

print(balance)

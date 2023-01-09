year, month, day, hour, minute,second= input("연,월,일,시,분,초를 입력하세요.").split()
print(year, month, day,sep='-',end='T')
print(hour,minute,second,sep=':')
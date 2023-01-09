start = int(input("숫자를 입력하세요."))
end = start-1

for i in range(start):
    for j in range(start+i):
        if j < end:
            print(' ',end = '')
        else:
            print('*',end='')
    print()
    end-=1

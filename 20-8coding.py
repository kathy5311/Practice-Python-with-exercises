start, end = map(int, input("숫자를 입력하세요.").split())

for i in range(start,end+1):
    if i%5==0 and i%7==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Fizz')
    elif i%7==0:
        print('Buzz')
    else:
        print(i)
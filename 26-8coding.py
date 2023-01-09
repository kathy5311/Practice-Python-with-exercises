c,d=map(int,input().split())
a= {i for i in range(1,c+1) if c%i==0}
b= {j for j in range(1,d+1) if d%j==0}
divisor = a&b

result=0
if type(divisor)==set:
    result = sum(divisor)

print(result)
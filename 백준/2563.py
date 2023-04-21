a= int(input())
b=[[0]*101 for _ in range(101)]
for _ in range(a):
    x,y=map(int,input().split())
    for i in range(10):
        for j in range(10):
            b[x+i][y+j]=1
result=0
for i in b:
    result+=sum(i)
print(result)

a=list(map(int,input().split()))
b=[1,1,2,2,2,8]
result=list(map(lambda a,b: b-a,a,b))
print(*result)


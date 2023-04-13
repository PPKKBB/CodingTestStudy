a,b=map(int,input().split())
c=[0]*a
for i in range(b):
    x,y,z=map(int,input().split())
    for j in range(x-1,y):
        c[j]=z
print(*c)

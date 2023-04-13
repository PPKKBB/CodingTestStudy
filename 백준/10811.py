a,b=map(int,input().split())
c=[i+1 for i in range(a)]
for _ in range(b):
    x,y=map(int,input().split())
    c[x-1:y] = reversed(c[x-1:y])
print(*c)

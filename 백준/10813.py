a,b=map(int,input().split())
c=[i+1 for i in range(a)]
for i in range(b):
    x,y=map(int,input().split())
    c[x-1],c[y-1] = c[y-1],c[x-1]
print(*c)

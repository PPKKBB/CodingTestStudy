a,b=map(int,input().split())
c=[i for i in range(0,a+1)]
for _ in range(b):
    x,y,z=map(int,input().split())
    c=c[:x]+c[z:y+1]+c[x:z]+c[y+1:]
print(*c[1:])


a,b=map(int,input().split())
c=[]
d=[]
for _ in range(a):
    c.append(list(map(int,input().split())))
for _ in range(a):
    d.append(list(map(int,input().split())))
for i in range(a):
    for j in range(b):
        print(c[i][j]+d[i][j],end=" ")
    print()

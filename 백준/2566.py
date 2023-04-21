a=[]
b=[]
for _ in range(9):
    a.append(list(map(int,input().split())))
b=list(map(max,a))
x=b.index(max(b))
c=a[x]
y=c.index(max(b))
print(max(b))
print(x+1,y+1)

a=int(input())
l=1
x=[]
y=[]
while a>l:
    a-=l
    l+=1
if l%2==0:
    for i in range(l):
        x.append(i+1)
    for j in range(l,0,-1):
        y.append(j)
else:
    for i in range(l,0,-1):
        x.append(i)
    for j in range(l):
        y.append(j+1)
print(f"{x[a-1]}/{y[a-1]}")
    

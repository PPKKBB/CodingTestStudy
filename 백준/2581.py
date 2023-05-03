m=int(input())
n=int(input())
r=[]
for i in range(m,n+1):
    x=[]
    for j in range(1,i+1):
        if i%j==0:
            x.append(j)
    if len(x)==2:
        r.append(i)
if len(r)>0:
    print(sum(r))
    print(min(r))
else:
    print("-1")

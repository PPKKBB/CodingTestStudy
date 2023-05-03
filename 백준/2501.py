a,b=map(int,input().split())
x=[]
for i in range(a+1):
    if a%(i+1)==0:
        x.append(i+1)
if len(x)<b:
    print("0")
else:
    print(x[b-1])

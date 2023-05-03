a=int(input())
b=list(map(int,input().split()))
cnt=0
for i in b:
    x=[]
    for j in range(1,i+1):
        if i%j==0:
            x.append(j)
    if len(x)==2:
        cnt+=1
print(cnt)         

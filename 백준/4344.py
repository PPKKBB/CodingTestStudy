a=int(input())
for i in range(a):
    count=0
    b=list(map(int,input().split()))
    avg=sum(b[1:])/b[0]
    for i in range(len(b[1:])):
        if avg<b[i+1]:
            count+=1
    result=count/b[0]*100
    print("{:.3f}%".format(result))

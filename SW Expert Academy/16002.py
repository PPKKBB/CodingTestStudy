for T in range(1,11):
    cnt=0
    N=int(input())
    x=list(map(int,input().split()))
    for i in range(2,len(x)-2):
        y=[x[i-2],x[i-1],x[i+1],x[i+2]]
        if x[i]>max(y):
            cnt+=x[i]-max(y)
    print(f"#{T} {cnt}")
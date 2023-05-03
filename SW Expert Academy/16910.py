T=int(input())
for i in range(T):
    cnt=0
    N=int(input())
    for x in range(-N,N+1):
        for y in range(-N,N+13):
            if x*x+y*y<=N*N:
                cnt+=1
    print(f"#{i+1} {cnt}")
import math
T=int(input())
for i in range(T):
    x=[]
    N=int(input())
    for j in range(1,int(math.sqrt(N)+1)):  # 효율적인 약수 구하는 방법
        if N%j==0:
            x.append([j,N//j])
    x=map(sum,x)
    print(f"#{i+1} {min(x)-2}")
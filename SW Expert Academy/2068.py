a=int(input())
for i in range(a):
    x=list(map(int,input().split()))
    x.sort()
    print(f"#{i+1} {x[-1]}")

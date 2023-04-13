X=int(input())
N=int(input())
y=0
for i in range(N):
    a,b=map(int,input().split())
    y+=a*b
print("Yes" if X==y else "No")
    

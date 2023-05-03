a=int(input())
b=list(map(int,input().split()))
b.sort()
mid=(len(b)+1)//2-1
print(b[mid])

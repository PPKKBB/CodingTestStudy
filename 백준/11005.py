import sys
tmp='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n,b=map(int,sys.stdin.readline().split())
r=''
while n>0:
    r+=str(tmp[n%b])
    n=n//b
print(r[::-1])

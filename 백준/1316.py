a=int(input())
cnt=0
result=0
for _ in range(a):
    b=input()
    for i in range(len(b)-1):
        if b[i+1] == b[i]:
            cnt+=1
            continue
        else:
            if b[i+1] not in b[:i+1]:
                cnt+=1
                continue
            else:
                break
    if cnt==len(b)-1:
        result+=1
    cnt=0
print(result)

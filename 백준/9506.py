import sys
while True:
    x=[]
    a=int(sys.stdin.readline())
    if a==-1:
        break
    for i in range(a-1):
        if a%(i+1)==0:
            x.append(i+1)
    if a==sum(x):
        print(f"{a} = ",end="")
        for i in x:
            if i == x[len(x)-1]:
                print(f"{i}")
            else:
                print(f"{i} + ",end="")
    else:
        print(f"{a} is NOT perfect.")

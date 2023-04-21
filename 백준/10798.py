a=[]
for i in range(5):
    b=input()
    a.append(b)
for i in range(15):
    for j in range(5):
        if i<len(a[j]):
            print(a[j][i],end="")

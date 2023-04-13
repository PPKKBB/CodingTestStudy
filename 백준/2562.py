a=[]
for i in range(9):
    a.append(int(input()))
for j in range(9):
    if max(a)==a[j]:
        print(a[j])
        print(j+1)

a=input().upper()
b=[]
m=[]
for i in range(65,91):
    b.append(a.count(chr(i)))
for j in range(len(b)):
    if b[j] == max(b):
        m.append(j)
if len(m)>1:
    print("?")
else:
    print(chr(m[0]+65))

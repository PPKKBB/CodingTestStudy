a=input()
b=[]
for i in range(97,123):
    b.append(a.find(chr(i)))
print(*b)

a=input()
r=0
b=[[],[],[],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
for i in a:
    for j in range(len(b)):
        if i in b[j]:
            print
            r+=j
print(r)
            

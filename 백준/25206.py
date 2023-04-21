score={
    "A+":4.5,
    "A0":4.0,
    "B+":3.5,
    "B0":3.0,
    "C+":2.5,
    "C0":2.0,
    "D+":1.5,
    "D0":1.0,
    "F":0.0
    }
point=0
cnt=0
for _ in range(20):
    a=list(map(str,input().split()))
    if a[2] =="P":
        continue
    point+=float(a[1])*score[a[2]]
    cnt+=int(float(a[1]))
result=point/cnt
print("{:.7}".format(result))

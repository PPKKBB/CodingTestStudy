a=int(input())
day_list=[31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(a):
    x=input()
    print(f"#{i+1}",end=" ")
    year=x[:4]
    month=x[4:6]
    day=x[6:]
    if int(month)<1 or int(month)>12 or int(day)<1 or int(day)>day_list[int(month)-1]:
        print("-1")
        continue
    else:
        print(f"{year}/{month}/{day}")

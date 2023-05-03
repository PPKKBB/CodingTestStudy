TC=int(input())
for T in range(1,TC+1):
    x,y = map(int,input().split())
    x=list(map(int, str(x)))
    max_index_list = list(filter(lambda a: x[a] == max(x), range(len(x))))
    min_index_list = list(filter(lambda a: x[a] == min(x), range(len(x))))
    z=[]
    for i in max_index_list:
        for j in min_index_list:
            b=x.copy()
            b[i], b[j] = b[j], b[i]
            b=list(map(str, b))
            s="".join(b)
            z.append(s)
    print(*z)

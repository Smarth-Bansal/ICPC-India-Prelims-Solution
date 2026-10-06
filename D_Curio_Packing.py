def find_nth(s, ch, n):
    idx = -1
    for _ in range(n):
        idx = s.find(ch, idx + 1)
        if idx == -1:
            return -1
    return idx

for _ in range(int(input())):
    n,k=map(int,input().split())
    curio=input()
    idx=find_nth(curio,"G",k+2)
    if idx==-1:
        print("YES")
    else:
        summer=0
        for i in range(idx+1,n):
            summer+=1 if curio[i]=="G" else 2
        print("NO" if summer>k else "YES")
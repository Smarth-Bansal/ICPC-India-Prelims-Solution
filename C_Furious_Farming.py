for _ in range(int(input())):
    n,m=map(int, input().split())
    x=list(map(int,input().split()))
    x.sort()
    a=x[0]-1
    b=n-x[m-1]
    maxxer=0
    for i in range(m-1):
        gap=x[i+1]-x[i]-1
        if gap>maxxer:
            maxxer=gap
    ans1=2*a+max(b,maxxer-a)
    ans2=2*b+max(a,maxxer-b)
    print(min(ans1,ans2))
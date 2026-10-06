for _ in range(int(input())):
    x,a,b=map(int,input().split())
    cost=0
    if x<80:
        cost+=((80-x)*a)
        x=80
    cost+=((100-x)*b)
    print(cost)

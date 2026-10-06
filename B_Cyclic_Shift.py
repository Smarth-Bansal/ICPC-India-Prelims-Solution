for _ in range (int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    diff=[]
    for i in range(1,n+1):
        diff.append(abs(a[i%n]-a[(i+1)%n]))
    diff.sort()
    print(diff[-2])
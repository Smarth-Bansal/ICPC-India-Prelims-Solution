M=998244353
N=200001
inv=[0,1]+[0]*N
for i in range(2,N+1):
    inv[i]=(M-(M//i)*inv[M%i]%M)%M
H=[0]*(N+1)
for i in range(1,N+1):
    H[i]=(H[i-1]+inv[i])%M
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n):
        ans=(ans+a[i]*(H[i]+H[n-1-i]))%M
    print(ans)
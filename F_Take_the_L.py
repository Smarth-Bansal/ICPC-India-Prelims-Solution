for _ in range(int(input())):
    n = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(n)]
    pts.sort()
    c1 = 0
    for i in range(n - 1):
        if pts[i][1] > pts[i + 1][1]:
            c1 += 1
    pts.sort(key=lambda t: t[1])
    c2 = 0
    for i in range(n - 1):
        if pts[i][0] > pts[i + 1][0]:
            c2 += 1
    print("YES" if min(c1, c2) <= 1 else "NO")
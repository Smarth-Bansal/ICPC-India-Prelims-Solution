for _ in range(int(input())):
    n, c = map(int, input().split())
    p = [int(x) - 1 for x in input().split()]
    a = list(map(int, input().split()))

    visited = [False] * n
    total = 0
    for i in range(n):
        if visited[i]:
            continue
        vals = []
        j = i
        while not visited[j]:
            visited[j] = True
            vals.append(a[j])
            j = p[j]
        L = len(vals)
        if L == 1:
            total += vals[0]
            continue

        vals.sort(reverse=True)
        best = 0
        pref = 0
        for j in range(1, L - 1):
            pref += vals[j - 1]
            val = pref - j * c
            if val > best:
                best = val
        full = sum(vals) - (L - 1) * c
        if full > best:
            best = full
        total += best
    print(total)
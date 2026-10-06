MOD = 998244353

for _ in range(int(input())):
    n = int(input())
    a = [int(x) - 1 for x in input().split()]
    idx = [[] for _ in range(n)]
    for i in range(n):
        idx[a[i]].append(i)

    if any(len(v) > 6 for v in idx) or len(idx[n - 1]) >= 2:
        print(0)
        continue

    def checkL(l, r, cur):
        length = r - l + 1
        i = l - 1
        pos = set()
        if 2 * i <= r:
            pos.add(2 * i)
        if 2 * i + 1 <= r:
            pos.add(2 * i + 1)
        if i <= length and 2 * length >= r:
            pos.add(2 * length)
        if i <= length and 2 * length - 1 >= r:
            pos.add(2 * length - 1)
        if n - 2 * length - 1 <= i:
            pos.add(n - 2 * length - 1)
        if n - 2 * length <= i:
            pos.add(n - 2 * length)
        for x in cur:
            if x not in pos:
                return False
        return True

    def checkR(l, r, cur):
        mapped = [n - x - 1 for x in cur]
        return checkL(n - r - 1, n - l - 1, mapped)

    prev = [1]
    for length in range(n - 1, 0, -1):
        cur_idx = idx[n - length - 1]
        new = [0] * (n - length + 1)
        for l in range(n - length + 1):
            r = l + length - 1
            v = 0
            if l >= 1 and checkL(l, r, cur_idx):
                v += prev[l - 1]
            if r + 1 < n and checkR(l, r, cur_idx):
                v += prev[l]
            new[l] = v % MOD
        prev = new

    if len(idx[n - 1]) == 1:
        m = idx[n - 1][0]
        if m == 0:
            print(prev[0] % MOD)
        elif m == n - 1:
            print(prev[n - 1] % MOD)
        else:
            print(0)
    else:
        print(sum(prev) % MOD)
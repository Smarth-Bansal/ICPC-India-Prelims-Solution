for _ in range(int(input())):
    c00, c01, c10, c11 = map(int, input().split())
    n = c00 + c01 + c10 + c11
    if n == 1:
        if c00:
            print("00")
        elif c01:
            print("01")
        elif c10:
            print("10")
        else:
            print("11")
        continue
    best = ""
    names = ["00", "01", "10", "11"]
    for l in range(4):
        cnt = [c00, c01, c10, c11]
        if cnt[l] == 0:
            continue
        cnt[l] -= 1
        a, b, c, d = cnt
        ka = min(a, d + b)
        xd = min(d, ka)
        bd1 = ka - xd
        dl = d - xd
        bl = b - bd1
        if dl >= bl:
            kb = bl
            bd2 = 0
            xd2 = kb
        else:
            kb = (bl + dl) // 2
            xd2 = dl
            bd2 = kb - dl
        r = (bl - kb - bd2) + (dl - xd2)
        zeros = a + ka + c
        res = "0" * zeros + "01" * kb + "1" * r + names[l]
        if best == "" or res < best:
            best = res
    print(best)
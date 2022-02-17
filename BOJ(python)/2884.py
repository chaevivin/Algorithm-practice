h, m = map(int, input().split())

if m < 45:
    if h == 0:
        h = 24
    h = h - 1
    m = (m + 60) - 45
    print("%d %d" % (h, m))
else:
    m = m - 45
    print("%d %d" % (h, m))

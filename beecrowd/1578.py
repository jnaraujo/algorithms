qnt_m = int(input())

for i in range(qnt_m):
    row = col = int(input())

    max_col = [0] * col 

    m = []
    for j in range(row):
        m.append(list(map(int, input().split())))

    for r in range(row):
        for c in range(col):
            m[r][c] = m[r][c] ** 2
            if len(str(m[r][c])) > max_col[c]:
                max_col[c] = len(str(m[r][c]))

    print("Quadrado da matriz #{}:".format(i+4))
    for r in range(row):
        for c in range(col):
            pad = 0
            if c > 0:
                pad = 1
            print("{}".format(str(m[r][c]).rjust(max_col[c]+pad)), end="")
        print()
    if i < qnt_m - 1:
        print()


# teste
# 1
# 2
# 7 12
# 1024 1
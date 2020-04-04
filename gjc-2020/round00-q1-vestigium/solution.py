def solve(m):
    trace = 0
    rows = 0
    cols = 0

    for ij in range(len(m)):
        trace += m[ij][ij]

    for i in range(len(m)):
        s = set(m[i])
        v = set(range(1, len(m)+1))
        if len(v - s) != 0:
            rows += 1

    for j in range(len(m)):
        col = []
        for i in range(len(m)):
            col.append(m[i][j])
        s = set(col)
        v = set(range(1, len(m)+1))
        if len(v - s) != 0:
            cols += 1

    return trace, rows, cols


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        m = []
        for i in range(N):
            row = [int(c) for c in input().split(' ')]
            m.append(row)
        trace, r, c = solve(m)
        print('Case #{}: {} {} {}'.format(t, trace, r, c))

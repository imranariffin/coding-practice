def solve(s):
    groups = []
    g = []
    for i, d in enumerate(s):
        if not g:
            g.append([d, i])
        elif d in g[-1][0]:
            g.append([d, i])
        else:
            groups.append(g)
            g = [[d, i]]
    if g:
        groups.append(g)

    tokens = [
        (
            int(g[0][0]) * -1,
            g[0][0] * len(g),
            g[0][1],
            g[len(g)-1][1]
        )
        for g in groups
    ]

    result = []
    while tokens:
        _, token, i, j = tokens.pop()
        d = int(token[0])
        left = d - int(s[i-1]) if i > 0 else d
        right = d - int(s[j+1]) if j < len(s) - 1 else d
        result.insert(0, '(' * left + token + ')' * right)
    return ''.join(result)


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        a = solve(input())
        print('Case #{}: {}'.format(t, a))

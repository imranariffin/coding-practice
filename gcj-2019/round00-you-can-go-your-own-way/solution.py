def solve(n, lydia):
    path = []
    for step in lydia:
        if step == 'E':
            path.append('S')
        else:
            path.append('E')
    return ''.join(path)


t = int(input())
for i in range(1, t+1):
    print('Case #{}: {}'.format(i, solve(input(), input())))

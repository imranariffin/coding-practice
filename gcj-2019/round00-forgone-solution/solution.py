from collections import defaultdict
from sys import stdin


def forgone_solution(n):
    mem = defaultdict(list)
    p = 1
    while n > 0:
        n, d = divmod(n, 10)
        if d == 4:
            mem[p].append(2)
            mem[p].append(2)
        else:
            mem[p].append(d)
        p *= 10

    a = 0
    for p in mem:
        a += mem[p].pop() * p
    b = 0
    for p in mem:
        if mem[p]:
            b += mem[p].pop() * p

    return a, b


if __name__ == '__main__':
    for i, line in enumerate(stdin):
        a, b = forgone_solution(int(line))
        print(f'Case #{i+1}: {a} {b}')

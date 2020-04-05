def forgone_solution(n):
    a = int(n.replace('4', '3'))
    return a, int(n) - a


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t+1):
        a, b = forgone_solution(input())
        print(f'Case #{i}: {a} {b}')


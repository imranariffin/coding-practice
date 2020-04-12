import sys


def solve(A, B, N):
    tries = 0
    guess = A + (B - A) // 2
    while tries < N:
        print(guess, flush=True)
        ans = input()
        if ans == 'TOO_BIG':
            B = guess
            guess = A - (B - A) // 2
        elif ans == 'TOO_SMALL':
            A = guess
            guess = A + (B - A) // 2
        else:
            break
        tries += 1


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        A, B = [int(w) for w in input().split(' ')]
        N = int(input())
        solve(A, B, N)


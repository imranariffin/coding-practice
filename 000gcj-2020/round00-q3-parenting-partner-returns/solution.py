from heapq import heapify, heappop


class Task:
    def __init__(self, s, e, order):
        self.s = int(s)
        self.e = int(e)
        self.order = order
        self.assignee = None

    def __lt__(self, other):
        if self.s != other.s:
            return self.s < other.s
        return self.e < other.e

    def __str__(self):
        line = ''
        for i in range(0, self.e, 1):
            if i < self.s:
                line += '_'
            else:
                line += '*'
        return line

    def __repr__(self):
        return '(s={}, e={}, order={})'.format(self.s, self.e, self.order)


def solve(tasks):
    tasks = [Task(t[0], t[1], i) for i, t in enumerate(tasks)]
    heap = [t for t in tasks]
    heapify(heap)

    #print(tasks)
    t = heappop(heap)
    maxendc = max(t.e, 0)
    maxendj = 0
    #print(t)
    t.assignee = 'C'
    i = 0
    while heap:
        t = heappop(heap)
        #print(t)
        #print('t.s={}, maxendc={}, maxendj={}'.format(t.s, maxendc, maxendj))

        if t.s >= maxendc:
            t.assignee = 'C'
        elif t.s >= maxendj:
            t.assignee = 'J'
        else:
            return 'IMPOSSIBLE'

        if t.assignee == 'J':
            maxendj = max(maxendj, t.e)
        else:
            maxendc = max(maxendc, t.e)
        i += 1

    tasks.sort(key=lambda t: t.order)
    result = [t.assignee for t in tasks]

    return ''.join(result)


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        tasks = []
        for n in range(N):
            s, e = input().split(' ')
            tasks.append((s, e,))
        print('Case #{}: {}'.format(t, solve(tasks)))


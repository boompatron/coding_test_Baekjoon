import sys
from collections import deque


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    in_degree, graph = [0 for _ in range(n + 1)], [[] for _ in range(n + 1)]
    while m:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        in_degree[b] += 1
        graph[a].append(b)
        m -= 1
    dq, ans = deque(), deque()
    for d in enumerate(in_degree[1:], start=1):
        if not in_degree[d[0]]:
            dq.appendleft(d[0])
    while dq:
        cur = dq.pop()
        ans.append(cur)
        for g in graph[cur]:
            in_degree[g] -= 1
            if not in_degree[g]:
                dq.appendleft(g)
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    solution()

import sys
readline = sys.stdin.readline

n, q = map(int, readline().split())
vis = [False] * (n + 1)
i = 1
for _ in range(q):
    op = list(map(int, readline().split()))
    if op[0] == 1:
        pass
    elif op[0] == 2:
        vis[op[1]] = True
    else:
        while vis[i]:
            i += 1
        print(i)

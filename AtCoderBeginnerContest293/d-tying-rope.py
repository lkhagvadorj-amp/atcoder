N, M = map(int, input().split())

for i in range(M):
    A, B, C, D = map(int, input().split())
    A, C = A-1, C-1
    if B == D:
        uf.union(A, C)
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

visited = set()
count = 0

def dfs(i, j):
    global count, visited
    if i == H and j == W:
        count += 1
        return
    if i < H and A[i+1-1][j-1] not in visited:
        visited.add(A[i+1-1][j-1])
        dfs(i+1, j)
        visited.remove(A[i+1-1][j-1])
    if j < W and A[i-1][j+1-1] not in visited:
        visited.add(A[i-1][j+1-1])
        dfs(i, j+1)
        visited.remove(A[i-1][j+1-1])

visited.add(A[0][0])
dfs(1, 1)

print(count)

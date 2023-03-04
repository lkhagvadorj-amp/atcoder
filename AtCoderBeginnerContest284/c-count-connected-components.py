import sys
input = lambda: sys.stdin.readline().rstrip()
 
def dfs(graph,start):
    stack = []
    result = []
    stack.append(start)
    visited = set()
    visited.add(start)
    while(len(stack)>0):
        currentVertex = stack.pop()
        result.append(currentVertex)
        for neighbor in graph[currentVertex]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    return result

n,m = map(int,input().split())
graph = {}
for i in range(n):
    graph[i+1] = []
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

exist = []
ans =0
for i in range(1,n+1):
    result = []
    if i not in exist:
        result = dfs(graph,i)
        ans += 1
        for x in result:
            exist.append(x)
print(ans)
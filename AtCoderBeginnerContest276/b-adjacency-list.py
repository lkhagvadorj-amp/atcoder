n,m = map(int,input().split())

road = {}
for i in range(n):
    road[i+1] = []
for i in range(m):
    a,b = map(int,input().split())
    road[a].append(b)
    road[b].append(a)

print(road)
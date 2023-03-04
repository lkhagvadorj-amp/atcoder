u={}
for s in[*open(a:=0)][1:]:
    x,y=map(r:=lambda x:x in u and r(u[x])or x,s.split())
    a|=x==y
    u[y]=x
print('YNeos'[a::2])

# import sys

# def solve():
# 	input = sys.stdin.readline
# 	N = int(input())
# 	parent = [-1] * N * 2
# 	m = {}
# 	n = 0
# 	for _ in range(N):
# 		s, t = input().split()
# 		m[s] = t

# 	dis = set()
# 	for i in m:
# 		start = i
# 		current = i
# 		while current:
# 			if current in dis:
# 				break
# 			dis.add(current)
# 			current = m.get(current, None)
# 			if current == start:
# 				return "No"
# 	return "Yes"

# print(solve())


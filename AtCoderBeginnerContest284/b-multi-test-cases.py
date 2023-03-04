import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    s = [i for i in a if i%2==1]
    print(len(s))
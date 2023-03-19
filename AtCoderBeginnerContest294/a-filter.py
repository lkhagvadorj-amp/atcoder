N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    if A[i]%2 == 0:
        print(str(A[i]) + ' ')

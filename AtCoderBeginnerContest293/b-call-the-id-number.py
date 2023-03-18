N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))

called = [False] * (N)

for i in range(N):
    if not called[i]:
        called[A[i]] = True

ans = [str(i+1) for i in range(N) if not called[i]]

print(len(ans))
print(" ".join(ans))
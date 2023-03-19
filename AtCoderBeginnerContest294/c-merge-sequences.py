from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# concatenate A and B to form C
C = A + B

# sort the sequence C in ascending order
C.sort()

# find the positions of the elements in A and B in C using binary search
for element in A + B:
    index = bisect_left(C, element)
    print(index + 1, end=' ')
print()

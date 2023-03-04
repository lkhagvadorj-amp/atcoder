def solve():
    N = int(input())
    A = [0]+list(map(int,input().split()))
 
    Q = int(input())
    answer  =[]
    for q in range(1,Q+1):
        mode,*value = map(int,input().split())
        if mode == 1:
            k,x = value
            A[k] = x
        else:
            k, = value
            answer.append(A[k])
 
    return answer
 
import sys
input = sys.stdin.readline
write = sys.stdout.write
 
write("\n".join(map(str,solve())))
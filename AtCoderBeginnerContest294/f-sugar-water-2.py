def binary_search(ok,ng,error,test):
    """
    :param ok: solve(x) = True を必ず満たす点
    :param ng: solve(x) = False を必ず満たす点
    """
    while abs(ok-ng)>error:
        mid=(ok+ng)/2
        if test(mid):
            ok=mid
        else:
            ng=mid
    return ok

##############################################################

import sys
input = sys.stdin.readline



def example():
    global input
    example = iter(
        """
4 5 10
5 4
1 6
7 4
9 8
2 2
5 6
6 7
5 3
8 1


        """
            .strip().split("\n"))
    input = lambda: next(example)

# example()


N,M,K=map(int, input().split())
A=[]
for _ in range(N):
    a,b=map(int, input().split())
    A.append((a,b))
B=[]
for _ in range(M):
    a,b=map(int, input().split())
    B.append((a,b))




def test(x):
    AA=[]
    for i in range(N):
        a,b=A[i]
        AA.append(a*100-(a+b)*x)
    AA.sort(reverse=True)

    BB=[]
    for i in range(M):
        a,b=B[i]
        BB.append(a*100-(a+b)*x)
    BB.sort(reverse=True)

    r=M-1
    res=0
    for l in range(N):
        a=AA[l]
        while r>=0 and a+BB[r]<0:
            r-=1
        res+=(r+1)
    return res>=K



print(binary_search(0,100,10**-9,test))
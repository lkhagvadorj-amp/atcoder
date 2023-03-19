import sys
import numpy as np

def solve(n, A, B):
    a, b = A.shape[0], B.shape[0]
    ans = 0
    ai, bi = 0, 0
    END = np.full(2, 1 << 60, np.int64)
    while ai != a or bi != b:
        xa, ya = A[ai] if ai != a else END
        xb, yb = B[bi] if bi != b else END
        j = min(ya, yb)
        ya -= j
        yb -= j
        if ya == 0:
            ai += 1
        else:
            A[ai, 1] = ya
        if yb == 0:
            bi += 1
        else:
            B[bi, 1] = yb
        if xa == xb: ans += j
    return ans







def main():
    n, a, b = map(int, input().split())
    IN = np.fromstring(sys.stdin.read(), np.int64, sep=' ').reshape(-1, 2)
    A = IN[:a]
    B = IN[a:]
    print(solve(n, A, B))




if __name__ == '__main__':
    if sys.argv[-1] == 'ONLINE_JUDGE':
        from numba.pycc import CC
        cc = CC('my_module')
        cc.export('solve', 'i8(i8, i8[:,:], i8[:,:])')(solve)
        cc.compile()
        exit()
    from my_module import solve
    main()
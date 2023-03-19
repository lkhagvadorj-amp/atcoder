import sys
input = sys.stdin.buffer.readline

N = int(input())
A = [0] * N
G = [[] for _ in range(N)]
E = {}
Enumber = []
for _ in range(N-1):
    a, b, c = map(int,input().split())
    if a > b: a, b = b, a
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
    E[a<<20|b] = c
    Enumber.append(a<<20|b)

def EulerTour(root):
    ete = []
    etv = []
    parents = [None] * N
    in_ = [0] * N
    out = [0] * N
    depth = [None]*N
    q = [~root, root]
    depth[root] = 0
    i = 0
    while q:
        v = q.pop()
        if v >= 0:
            ete.append(v)
            etv.append(v)
            in_[v] = i
            for vv in G[v]:
                if depth[vv] is not None: continue
                depth[vv] = depth[v] + 1
                parents[vv] = v
                mi, ma = min(v,vv), max(v, vv)
                A[vv] = E[mi<<20|ma]
                q.append(~vv)
                q.append(vv)
        else:
            ete.append(~v)
            etv.append(parents[~v])
            out[~v] = i
        i += 1
    etv.pop()
    return ete, etv, in_, out, depth

class SparseTable():
    def __init__(self, arr, op=min):
        self.op = op
        self.n = len(arr)
        self.h = self.n.bit_length()
        self.table = [[0] * self.n for _ in range(self.h)]
        self.table[0] = [a for a in arr]
        for k in range(1, self.h):
            t, p = self.table[k], self.table[k - 1]
            l = 1 << (k - 1)
            for i in range(self.n - l * 2 + 1):
                t[i] = op(p[i], p[i + l])

    def query(self, l, r):
        k = (r - l).bit_length() - 1
        return self.op(self.table[k][l], self.table[k][r - (1 << k)])
root = 0
ete, etv, in_, out, depth = EulerTour(root)
arr = [depth[v]<<20|v for v in etv]
st = SparseTable(arr)
mask = (1<<20)-1
def LCA(u, v):
    x, y = in_[u], in_[v]
    if x > y: x, y = y, x
    res = st.query(x, y+1)
    return res&mask



class BIT:
    def __init__(self, n, nums=None):
        self.n = n
        self.size = 1<<n.bit_length()
        self.arr = [0] * (self.size+1)
        if nums: self._build(nums)
    def _build(self, nums):
        for i in range(1, self.n + 1):
            self.arr[i] += nums[i - 1]
        for i in range(1, self.size+1):
            j = i + (i & -i)
            if j <= self.size: self.arr[j] += self.arr[i]
    def add(self, idx, val): # nums[idx] += val
        idx += 1
        while idx <= self.size:
            self.arr[idx] += val
            idx += idx & -idx
    def pref(self, qr): # sum(nums[:qr])
        ans = 0
        while qr >= 1:
            ans += self.arr[qr]
            qr -= qr & -qr
        return ans
    def lower_bound(self, w):
        if w <= 0: return 0
        x, r = 0, self.size
        while r > 0:
            if x+r <= self.size and self.arr[x+r] < w:
                w -= self.arr[x+r]
                x += r
            r >>= 1
        return x
    def __getitem__(self, idx): return self.sum(idx, idx+1)
    def sum(self, ql, qr): return self.pref(qr) - self.pref(ql) # sum(nums[ql:qr])
    def suff(self, ql): return self.pref(self.n) - self.pref(ql) # sum(nums[ql:])
arr = [0] * (N<<1)
for i, e in enumerate(ete):
    arr[i] += A[e]
    A[e] = -A[e]
bit = BIT(N<<1, arr)

res = []
Q = int(input())
for _ in range(Q):
    q, x, y = map(int,input().split())
    if q == 2:
        x -= 1
        y -= 1
        lca = LCA(x, y)
        res.append(bit.pref(in_[x]+1) + bit.pref(in_[y]+1) - (bit.pref(in_[lca]+1)<<1))
    else:
        x -= 1
        uv = Enumber[x]
        u, v = uv>>20, uv&((1<<20)-1)
        lca = LCA(u, v)
        if u == lca: x = v
        else: x = u
        tmp = bit[in_[x]]
        bit.add(in_[x], -tmp+y)
        tmp = bit[out[x]]
        bit.add(out[x], -tmp-y)
print('\n'.join(map(str, res)))
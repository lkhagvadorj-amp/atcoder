import sys

def fast_prime_factorization_many(lst):
    # 素因数分解（ロー法、複数）
    from subprocess import Popen, PIPE
    res = Popen(["factor"] + list(map(str, lst)), stdout=PIPE).communicate()[0].split(b"\n")[:-1]
    return [list(map(int, r.split()[1:])) for r in res]

def main():
    A = list(map(int, sys.stdin.buffer.read().split()))[1:]
    Factors = fast_prime_factorization_many(A)
    for factors in Factors:
        if factors[0] == factors[1]:
            print(" ".join([str(factors[0]), str(factors[2])]))
        elif factors[0] == factors[2]:
            print(" ".join([str(factors[0]), str(factors[1])]))
        else:
            print(" ".join([str(factors[1]), str(factors[0])]))
    
main()
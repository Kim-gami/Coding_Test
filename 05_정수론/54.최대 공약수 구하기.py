import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if N > M:
    k = gcd(N, M)
else:
    k = gcd(M, N)
for _ in range(k):
    print(1, end='')
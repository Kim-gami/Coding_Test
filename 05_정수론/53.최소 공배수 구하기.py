import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    G = gcd(a, b)
    print(a * b / G)


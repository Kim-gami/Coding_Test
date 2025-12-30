import sys
input = sys.stdin.readline

N = int(input())
MOD = 1000000007
D = [0] * 1000001
D[1] = 0
D[2] = 1

for i in range(3, N + 1):
    D[i] = (i - 1) * (D[i - 1] + D[i -1]) % MOD

print(D[N])
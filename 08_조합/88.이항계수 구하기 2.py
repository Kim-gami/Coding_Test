import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [[0 for j in range(N + 1)] for i in range(N + 1)]
MOD = 10007

for i in range(N + 1):
    A[i][0] = 1
    A[i][i] = 1

for i in range(2, N + 1):
    for j in range(1, i):
        A[i][j] = (A[i - 1][j] + A[i - 1][j - 1]) % MOD

print(A[N][K])

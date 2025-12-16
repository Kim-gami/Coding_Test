import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []* N
cnt = 0

for i in range(N):
    A[i] = int(input())

for i in range(N - 1, -1, -1):
    if A[i] <= M:
        cnt += int(M / A[i])
        M = M % A[i]

print(cnt)
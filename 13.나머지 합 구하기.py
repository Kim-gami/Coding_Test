import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * N
C = [0] * Q
S[0] = A[0]
answer = 0

for i in range(1, N):
    S[i] = S[i-1] + A[i]

print(S)

for i in range(N):
    remainder = S[i] % Q
    if remainder == 0:
        answer += 1
    C[remainder] += 1

print(C)

for i in range(Q):
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2)

print(answer)
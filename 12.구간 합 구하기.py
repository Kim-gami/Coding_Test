import sys
input = sys.stdin.readline
N, Q = map(int,input().split())
A = [[0] * (N+1)]
S = [[0] * (N+1) for _ in range(N+1)]

print(A)
print(S)

for i in range(N):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

print(A)

#합 배열
for i in range(1, N+1):
    for j in range(1, N+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + A[i][j]

print(S)

for _ in range(Q):
    a, b, c, d = map(int,input().split())
    print(S[c][d] - S[a-1][d] - S[c][b-1] + S[a-1][b-1])
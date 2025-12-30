import sys
input = sys.stdin.readline

T = int(input())
A = [[0 for j in range(31)] for i in range(31)]

for i in range(1, 31):
    A[i][1] = i
    A[i][0] = 1
    A[i][i] = 1

for i in range(1, 31):
    for j in range(2, 31):
        A[i][j] = A[i-1][j] + A[i -1][j -1]

for _ in range(T):
    N, M = map(int, input().split())
    print(A[N][M])
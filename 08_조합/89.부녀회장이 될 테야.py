import sys
input = sys.stdin.readline

N = int(input())
A = [[0 for j in range(15)] for i in range(15)]

for i in range(1, 15):
    A[i][1] = 1
    A[0][i] = i

for i in range(1, 15):
    for j in range(2, 15):
        A[i][j] = A[i][j-1] + A[i-1][j]

for i in range(N):
    q = int(input())
    m = int(input())
    print(A[q][m])
import sys
input = sys.stdin.readline

N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

for j in range(N-1):
    for i in range(N-j-1):
        if A[i] > A[i+1]:
            A[i], A[i + 1] = A[i + 1], A[i]

for i in range(N):
    print(A[i])
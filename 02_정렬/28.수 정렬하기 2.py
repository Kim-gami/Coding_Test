import sys
input = sys.stdin.readline
print = sys.stdout.write

def mergeSort(S, E):
    if E - S < 1: return
    M = int(S +(E - S) / 2)
    mergeSort(S, M)
    mergeSort(M + 1, E)
    for i in range(S, E + 1):
        tmp[i] = A[i]

    K = S
    index1 = S
    index2 = M + 1
    while index1 <= M and index2 <= E:
        if tmp[index1] > tmp[index2]:
            A[K] = tmp[index2]
            K += 1
            index2 += 1
        else:
            A[K] = tmp[index1]
            K += 1
            index1 += 1
    while index1 <= M:
        A[K] = tmp[index1]
        K += 1
        index1 += 1
    while index2 <= E:
        A[K] = tmp[index2]
        K += 1
        index2 += 1

N = int(input())
A = [0] * int(N + 1)
tmp = [0] * int(N + 1)

for i in range(1, N + 1):
    A[i] = int(input()))

mergeSort(1, N)

for i in range(1, N + 1):
    print(str(A[i]) + '\n')


import sys
input = sys.stdin.readline
print = sys.stdout.write

def mergeSort(S, E):
    global count
    if E - S < 1:return
    M = int(S + (E - S) / 2)
    mergeSort(S, M)
    mergeSort(M + 1, E)
    for i in range(S, E + 1):
        tmp[i] = A[i]

    K = S
    index1 = S
    index2 = M + 1
    while index1 <= M and index2 <= E:
        if A[index1] < A[index2]:
            A[K] = A[index1]
            K += 1
            count = count + index2 - K
            index1 += 1
        else:
            A[K] = A[index2]
            K += 1
            index2 += 1
    while index1 < M:
        A[K] = A[index1]
        K += 1
        index1 += 1
    while index2 <= E:
        A[K] = A[index2]
        K += 1
        index2 += 1

N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
tmp = [0] * (N + 1)
count = 0

mergeSort(1, N)
print(str(count))
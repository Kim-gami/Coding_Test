import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
start = 0
end = 0

for i in range(N):
    start = max(start, A[i])
    end += A[i]

while start <= end:
    middle = (start + end) // 2
    sum = 0
    count = 0
    for i in range(N):
        if sum + A[i] > middle:
            count += 1
            sum = 0
        sum += A[i]
    if sum != 0:
        count += 1
    if count > M:
        start = middle + 1
    else:
        end = middle - 1
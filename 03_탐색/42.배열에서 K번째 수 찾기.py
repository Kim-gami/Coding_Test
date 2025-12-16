import sys
input = sys.stdin.readline

N, K = map(int, input())
start = 1
end = K
ans = 0

while start < end:
    middle = (start + end) // 2
    cnt= 0
    for i in range(1,N + 1):
        cnt += min(int(middle / i), N)
    if cnt < K:
        start = middle + 1
    else:
        ans = middle
        end = middle -1

print(ans)
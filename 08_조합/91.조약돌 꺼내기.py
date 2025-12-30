import sys
input = sys.stdin.readline

probablilty = [0] * 51
M = int(input())
D = list(map(int, input().split()))
T = 0

for i in range(M):
    T += D[i]

K = int(input())
ans = 0

for i in range(0, M):
    if D[i] >= K:
        probablilty[i] = 1
        for k in range(0, K):
            probablilty[i] = probablilty[i] * (D[i] - k) / (T - k)
        ans += probablilty[i]

print(ans)


import sys, math
input = sys.stdin.readline

N, M = map(int, input().split())
check = [False] * (M - N + 1)

for i in range(2, int(math.sqrt(M) + 1)):
    pow = i * i
    start_index = int(N / pow)
    if N % pow != 0:
        start_index += 1
    for j in range(start_index, int(M / pow) + 1):
        check[int((j * pow) - N)] = True
count = 0

for i in range(0, M - N + 1):
    if not check[i]:
        count += 1

print(count)


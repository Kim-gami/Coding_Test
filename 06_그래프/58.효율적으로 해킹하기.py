import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)


for i in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

def BFS(v):
    visit = [False] * (N + 1)
    queue = deque()
    queue.append(v)
    visit[v] = True
    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if not visit[i]:
                visit[i] = True
                answer[i] += 1
                queue.append(i)

for i in range(1, N + 1):
    BFS(i)

maxVal = max(answer)
for i in range(1, N + 1):
    if maxVal == answer[i]:
        print(i, end=' ')
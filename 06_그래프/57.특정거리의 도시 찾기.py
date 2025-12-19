import sys
from collections import deque
input = sys.stdin.readline

N, M, K ,X = map(int, input().split())
A = [[] for _ in range(N + 1)]
answer = []
visit = [-1] * (N + 1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visit[v] += 1
    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if visit[i] == -1:
                visit[i] = visit[now_node] + 1
                queue.append(i)

for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

BFS(X)

for i in range(N + 1):
    if visit[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)
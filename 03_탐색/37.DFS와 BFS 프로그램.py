from collections import deque
N, M, start = map(int, input().split())
A = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N + 1):
    A[i].sort()

def DFS(v):
    print(v, end = ' ')
    visit[v] = True
    for i in A[v]:
        if not visit[i]:
            DFS(i)

visit = [False] * (N + 1)
DFS(start)

def BFS(v):
    queue = deque()
    queue.append(v)
    visit[v] = True
    while queue:
        now_node = queue.popleft()
        print(now_node, end = ' ')
        for i in A[now_node]:
            if not visit[i]:
                visit[i] = True
                queue.append(i)

print()
visit = [False] * (N + 1)
BFS(start)
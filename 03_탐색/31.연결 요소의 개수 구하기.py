import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
visit = [False] * (N + 1)

def DFS(v):
    visit[v] = True
    for i in A[v]:
        if not visit[i]:
            DFS(i)

for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)
    A[E].append(S)

count = 0

for i in range(1, N+1):
    if not visit[i]:
        count += 1
        DFS(i)

print(count)


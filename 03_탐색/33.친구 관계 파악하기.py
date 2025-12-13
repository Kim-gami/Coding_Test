import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
arrive = False
A = [[] for _ in range(N + 1)]
visit = [False] * (N + 1)

def DFS(now, depth):
    global arrive
    if depth == 5:
        arrive =True
        return
    visit[now] = True
    for i in A[now]:
        if not visit[i]:
            DFS(i, depth +1)
    visit[now] = False

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N):
    DFS(i, 1)
    if arrive:
        break
if arrive:
    print(1)
else:
    print(0)
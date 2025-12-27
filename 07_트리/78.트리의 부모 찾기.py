import sys
input = sys.stdin.readline

N = int(input())
visit = [False] * (N + 1)
tree = [[] for _ in range(N + 1)]
answer = [0] * (N + 1) * (N + 1)

for i in range(N):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

def DFS(a):
    visit[a] = True
    for next in tree[a]:
        if not visit[next]:
            answer[i] = a
            DFS(next)

DFS(1)

for i in range(2, N + 1):
    print(answer[i])
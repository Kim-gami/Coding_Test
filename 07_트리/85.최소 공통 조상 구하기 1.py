import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(0, N - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

depth = [0] * (N + 1)
parent = [0] * (N + 1)
visit = [False] * (N + 1)

def BFS(node):
    queue = [node]
    visit[node] = True
    while queue:
        now_node = queue.pop(0)
        for next in tree[now_node]:
            if not visit[next]:
                visit[next] = True
                queue.append(next)
                parent[next] = now_node
                depth[next] = depth[now_node] + 1

BFS(1)

def excuteLCA(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    while depth[a] != depth[b]:
        a = parent[a]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a

M = int(input())
mydict = dict()
for _ in range(M):
    a, b = map(int, input().split())
    if not mydict.get((a, b), 0):
        mydict[(a, b)] = mydict[(b, a)] = excuteLCA(a, b)
    print(mydict.get((a, b)))
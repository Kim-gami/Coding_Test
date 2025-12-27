import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N)]
visit = [False] * N
answer = 0
p = list(map(int, input().split()))

for i in range(N):
    if p[i] != -1:
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i

def DFS(number):
    global answer
    visit[number] = True
    cNode = 0
    for i in tree[number]:
        if not visit[i] and i != deleteNode:
            cNode += 1
            DFS(i)
        if cNode == 0:
            answer += 1

deleteNode = int(input())

if deleteNode == root:
    print(0)
else:
    DFS(root)
    print(answer)
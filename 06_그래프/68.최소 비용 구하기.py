import sys
input = sys.stdin.readline
from queue import PriorityQueue

V = int(input())
E = int(input())
cost = [sys.maxsize] * (V + 1)
visit = [False] * (V + 1)
mList = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    mList[u].append((v, w))

start, end = map(int, input().split())

q = PriorityQueue()
cost[start] = 0
q.put((0, start))

while q.qsize() > 0:
    c, node = q.get()
    if visit[node]:
        continue
    visit[node] = True
    for tmp in mList[node]:
        next, value = tmp[0], tmp[1]
        if cost[next] > cost[node] + value:
            cost[next] = cost[node] + value
            q.put((cost[next], next))

print(cost[end])
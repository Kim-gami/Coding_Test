import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [0] * (N + 1)

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(N + 1):
    parent[i] = i

for i in range(M):
    q, a, b = map(int, input().split())
    if q == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("YES")
        else:
            print("NO")


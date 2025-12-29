import sys
input = sys.stdin.readline

N, M = map(int, input().split())

length = N
treeHeight = 0

while length != 0:
    length //= 2
    treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leafStartNode = treeSize // 2 - 1
tree = [sys.maxsize] * treeSize

for i in range(leafStartNode + 1, leafStartNode + N + 1):
    tree[i] = int(input())

def setTree(i):
    while i != 0:
        if tree[i // 2] > tree[i]:
            tree[i // 2] = tree[i]
        i -= 1

setTree(treeSize - 1)

def getMin(s, e):
    realMin = sys.maxsize
    while s <= e:
        if s % 2 == 1:
            realMin = min(realMin, tree[s])
            s += 1
        if e % 2 == 0:
            realMin = min(realMin, tree[e])
            e -= 1
        s = s // 2
        e = e // 2
    return realMin

for _ in range(M):
    s, e = map(int, input().split())
    s = s + leafStartNode
    e = e + leafStartNode
    answer = getMin(s, e)
    print(answer)
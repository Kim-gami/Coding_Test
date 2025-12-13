import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
visit = [False] * N
S = [0] * M

def backtrack(le):
    if le == M:
        print(' '.join(str(x + 1) for x in S))
        return

    for i in range(0, N):
        if not visit[i]:
            visit[i] = True
            S[le] = i
            backtrack(le + 1)
            visit[i] = False

backtrack(0)

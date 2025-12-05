N = 4
graph = [ [] for _ in range(N + 1)]
# print(graph)

N, E = map(int, input().split())
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

print(graph)

# 4 6
# 1 2 6
# 2 3 7
# 3 4 8
# 4 1 5
# 4 2 9
# 2 4 10
# [[], [(2, 6)], [(3, 7), (4, 10)], [(4, 8)], [( 1, 5), (2, 9)]]
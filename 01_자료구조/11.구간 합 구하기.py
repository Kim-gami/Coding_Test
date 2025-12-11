N, Q = map(int,input("데이터의 갯수, 질문 갯수 : ").split())
A = list(map(int,input("배열 입력 : ").split()))
S = [0]

for a in range(len(A)):
    S.append(A[a] + S[a])

print(S)

for _ in range(Q):
    i, j = map(int,input().split())
    print(S[j] - S[i-1])

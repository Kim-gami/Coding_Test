import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = [0]* N
myStack = []

for i in range(N):
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

for i in range(N):
    print(ans[i], end=' ')
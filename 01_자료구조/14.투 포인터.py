import sys
input = sys.stdin.readline

N = int(input())

start = 1
end = 1
su = 1
answer = 1

while end != N:
    if su == N:
        answer += 1
        end += 1
        su += end

    elif su < N:
        end += 1
        su += end

    elif su > N:
        su -= start
        start += 1

print(answer)

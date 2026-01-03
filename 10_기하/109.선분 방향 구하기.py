import sys
input = sys.stdin.readline

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())

CCW = (a1*b2 + a2*b3 + a3*b1) - (a2*b1 + a3*b2 + a1*b3)
if CCW < 0:
    print(-1)
elif CCW > 0:
    print(1)
else:
    print(0)
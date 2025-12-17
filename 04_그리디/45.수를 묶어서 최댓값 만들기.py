from queue import PriorityQueue

ppq = PriorityQueue()
mpq = PriorityQueue()
N = int(input())
one = 0
zero = 0

for i in range(N):
    data = int(input())
    if data > 1:
        ppq.put(-data)
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        mpq.put(data)

sum = 0

while ppq.qsize() > 1:
    first = -ppq.get()
    second = -ppq.get()
    sum += first * second

if ppq.qsize() > 0:
    sum += -ppq.get()

while mpq.qsize() > 1:
    first = mpq.get()
    second = mpq.get()
    sum += first * second

if mpq.qsize() > 0:
    if zero == 0:
        sum += mpq.get()

sum += one
print(sum)
#오름차순
A = [5, 3, 2, 4, 1]

A.sort()
# print(A)

A = [5, 3, 2, 4, 1]

B = sorted(A)
# print(A)
# print(B)

#내림차순
A = [5, 3, 2, 4, 1]

A.sort(reverse=True)
# print(A)

A = [5, 3, 2, 4, 1]

B = sorted(A, reverse=True)
# print(A)
# print(B)

#부호 반전 방법
A = [5, 3, 2, 4, 1]

B = [-x for x in A]
B.sort()
B = [-x for x in B]
print(B)
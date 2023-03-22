from random import randint
N = int(input("Введите число N"))
X = int(input("Введите число X"))
A = [randint(1, N) for x in range(1, N+1)]
number = 0
for i in range(N):
    if (X-A[i]) < X-number and X-A[i] > 0:
        number = i
print(A[number])
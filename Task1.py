from random import randint
N = int(input("Введите число N"))
X = int(input("Введите число X"))
A = [randint(1, N//2) for x in range(1, N+1)]
print(A)
print(A.count(X))
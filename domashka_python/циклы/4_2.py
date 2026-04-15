a = float(input("Введите действительное число a: "))
n = int(input("Введите натуральное число n: "))
S = 0
for i in range(1, n+1):
    S = 1 / (a ** (2 * i - 2))
print ("S = ", S)
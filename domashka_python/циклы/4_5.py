n = int(input("Введите количество элементов: "))
summ = 0
for i in range(n):
    x = float(input(f"Введите элемент {i+1}: "))
    summ += x ** 2  
print("Сумма квадратов элементов =", summ)
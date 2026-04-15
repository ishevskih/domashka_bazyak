from math import cos
from pandas import DataFrame

# Ввод параметров отрезка и шага
a = float(input("Введите начало отрезка a: "))
b = float(input("Введите конец отрезка b: "))
h = float(input("Введите шаг h: "))

# Генерация значений x с помощью цикла while
x_values = []
x = a
while x <= b + 1e-12:
    x_values.append(round(x, 10))
    x += h

# Вычисление значений функции F(x) = x·cos(1/x) + 2
y_values = []
for x in x_values:
    if abs(x) < 1e-12:
        y_values.append("не определено")
    else:
        try:
            val = x * cos(1.0 / x) + 2
            y_values.append(round(val, 6))
        except Exception:
            y_values.append("ошибка")

# Создание таблицы
df = DataFrame({
    "x": x_values,
    "F(x) = x·cos(1/x) + 2": y_values
})

# Вывод таблицы
print("\nРезультаты вычислений:")
print(df.to_string(index=False))
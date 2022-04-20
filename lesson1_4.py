"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

n = abs(int(input("Введите целое положительное число ")))
max_number = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max_number:
        max_number = n % 10
    if n > 9:
        continue
    else:
        print(f"Максимальное цифра в числе - {max_number}")
        break
 

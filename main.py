# # Введите трехзначное число
# n = int(input("Введите трехзначное число: "))

# # Проверка на трехзначность числа
# if 100 <= n <= 999:
#     # Получаем цифры числа
#     digit1 = n // 100
#     digit2 = (n % 100) // 10
#     digit3 = n % 10

#     # Находим сумму цифр
#     res = digit1 + digit2 + digit3

#     print("Сумма цифр числа", n, ":", res)
# else:
#     print("Введенное число не является трехзначным.")

# ---------
# n = int(input("Введите количество журавликов n: "))

# # Решение системы уравнений
# S = n // 6  # Поскольку P = S, делим общее количество журавликов поровну между Петей и Сережей
# P = S
# K = 4 * S

# print("Количество журавликов, сделанных Петей, Катей и Сережей соответственно:", P, K, S)
# ---------
# Введите номер билета
# n = input("Введите номер билета (шестизначное число): ")

# Проверка на корректность ввода
# if len(n) == 6 and n.isdigit():
#     # Получаем цифры номера билета
#     digits = [int(digit) for digit in n]

#     # Проверка на счастливость
#     if sum(digits[:3]) == sum(digits[3:]):
#         print("yes")
#     else:
#         print("no")
# else:
#     print("Некорректный ввод. Пожалуйста, введите шестизначное число.")

# ------------

# a = 3
# b = 2
# c = 4

# # Проверка разламывания по длине (стороне a)
# if c <= a or c <= b:
#     print("yes")
# elif c % a == 0 and c // a < b:
#     print("yes")
# elif c % b == 0 and c // b < a:
#     print("yes")
# else:
#     print("no")

# ------------

# def min_flips_to_align(coins):
#     # Считаем количество монеток, лежащих гербом вверх
#     count_heads = sum(coins)

#     # Минимальное количество переворотов - это минимум между гербами и решками
#     min_flips = min(count_heads, len(coins) - count_heads)

#     return min_flips

# # Пример использования:
# coins = [0, 1, 0, 1, 1, 0]
# result = min_flips_to_align(coins)
# print(result)

#coins = [0, 1, 0, 1, 1, 0]
# def min_f(coins):
#     count_g = 0
#     for coin in coins:
#         count_g += coin
#     min_f = min(count_g, len(coins) - count_g)
#     return min_f
# result = min_f(coins)
# print(result)

#min('coins'.count('0'), 'coins'.count('1'))


# count_0 = 0
    
# for coin in coins:
#     if coin == 0:
#         count_0 += 1
#     else:
#         count_1 += 1
    
# return min(count_0, count_1)

# S = int(input("Введите сумму S: "))
# P = int(input("Введите произведение P: "))

# pairs = []

# for X in range(1, S + 1):
#     Y = S - X

#     if X * Y == P and X <= Y:
#         pairs.append((X, Y))

# if pairs:
#     print("Возможные пары чисел:")
#     for pair in pairs:
#         print(pair[0], pair[1])
# else:
#     print("Нет подходящих пар чисел.")

# s = 12
# p = 27
# pairs = []
# for x in range(1, s + 1):
#     y = s - x
#     if x * y == p and x <= y:
#         print(x, y)

# s = 12
# p = 27
# for x in range(1, s + 1):
#     y = s - x
#     if x * y == p and x <= y:
#         print(x, y)

# n = 16
# c = 2
# for x in range(0, n // 2):
#     n = c ** x
    
#     print(n)

# n = 32
# c = 2

# x = 0
# while c ** x <= n:
#     rezultat = c ** x
#     print(rezultat)
#     x += 1



from ui import interface


if __name__ == '__main__':
    interface()
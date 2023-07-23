def find_numbers(S, P):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if x + y == S and x * y == P:
                return x, y

# Пример использования функции:
sum_hint = 45
product_hint = 200
result_x, result_y = find_numbers(sum_hint, product_hint)
print("Задуманные числа: X =", result_x, ", Y =", result_y)
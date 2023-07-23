number = int(input("Введите трехзначное число: "))

digit_1 = number // 100
digit_2 = (number // 10) % 10
digit_3 = number % 10

sum_of_digits = digit_1 + digit_2 + digit_3

print("Сумма цифр трехзначного числа:", sum_of_digits)

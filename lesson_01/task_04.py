# GeekBrains, 10/06/2020 Python essentials
# homework
# author: Karpov Artem, date: 2020-06-13
# lesson 01
# task 4: Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
# Для решения используйте цикл while и арифметические операции.
print("founder max digit in tne input number")
u_number = int(input("type the number: ")) # need error handler
max_digit = 0
sign = ""
if u_number < 0:
    u_number = -1 * u_number
    sign = "-"

d = u_number // 10
dd = u_number % 10
if dd > max_digit:
    max_digit = dd
while d > 0:
    d = d // 10
    dd = d % 10
    if dd > max_digit:
        max_digit = dd 
# print result
print(f"in the {sign}{u_number} max digit is {max_digit}")
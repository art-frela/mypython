# GeekBrains, 10/06/2020 Python essentials
# homework
# author: Karpov Artem, date: 2020-06-13
# lesson 01
# task 3: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. 
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
print("user input converter, number to n + nn + nnn = result")
u_str_number = input("type number for convert: ") 
u_number = int(u_str_number) # need error handler
sign = "+"
first_sign = ""
if u_number < 0:
    u_number = -1 * u_number
    u_str_number = str(u_number)
    first_sign = "-"
    sign = "-"
u_2nd_number = int(f"{u_str_number}{u_str_number}") # need error handler for negative numbers
u_3rd_number = int(f"{u_str_number}{u_str_number}{u_str_number}")
print(f"{first_sign}{u_str_number} {sign} {u_str_number}{u_str_number} {sign} {u_str_number}{u_str_number}{u_str_number} = {first_sign}{u_number + u_2nd_number + u_3rd_number}")
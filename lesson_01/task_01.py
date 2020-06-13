# GeekBrains, 10/06/2020 Python essentials
# homework
# author: Karpov Artem, date: 2020-06-13
# lesson 01
# task 1: Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел 
# и строк и сохраните в переменные, выведите на экран.

# simple vars
div = 5 #int(input("type devision: "))
dvd = 36
print(f'{dvd} // {div} = {dvd // div}')
print(f'{dvd} % {div} = {dvd % div}')
# user input
u_string = input("type some text: ")
print(f'you typed: {u_string}')
u_str_int = input("type some natural number: ")
u_int = int(u_str_int) # need error handler, if error happen program stopped...
print(f"you typed: {u_str_int} it's a number ;)")

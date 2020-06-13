# GeekBrains, 10/06/2020 Python essentials
# homework
# author: Karpov Artem, date: 2020-06-13
# lesson 01
# task 2: Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
# Используйте форматирование строк.
# user input
print("time prettify converter, number of seconds to hh:mm:ss format (without days, be patient)")
u_sec = int(input("type secons for prettify: ")) # need error handler
# processing
hrs = u_sec // 3600
minutes = (u_sec - hrs * 3600) // 60
seconds = (u_sec - hrs * 3600 - minutes * 60)
str_hrs = "0" + str(hrs)
if hrs > 9:
    str_hrs = str(hrs)
str_mins = "0" + str(minutes)
if minutes > 9:
    str_mins = str(minutes)
str_sec = "0" + str(seconds)
if seconds > 9:
    str_sec = str(seconds)
# printing
print(f"{u_sec} seconds -> {str_hrs}:{str_mins}:{str_sec}")
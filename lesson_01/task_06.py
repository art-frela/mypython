# GeekBrains, 10/06/2020 Python essentials
# homework
# author: Karpov Artem, date: 2020-06-13
# lesson 01
# task 6: Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22

# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
print("simplest running calculator, for daily gain +10%")
run_dist = float(input("type the distance in kilometers you can run today: ")) # need error handler
target_dist = float(input("type the distance in kilometers you want to run: ")) # need error handler
if target_dist <= run_dist or target_dist < 0 or run_dist < 0:
    print(f"you can run {target_dist:.2f}km today!") # need more useful text
    raise SystemExit
days = 1
print(f"\t{days}-day: {run_dist:.2f}km")
while target_dist > run_dist:
    run_dist *= 1.1
    days += 1
    print(f"\t{days}-day: {run_dist:.2f}km")

print(f"you can run {target_dist:.2f}km through {days} day(s)")
# GeekBrains, 10/06/2020 Python essentials
# homework
# author: Karpov Artem, date: 2020-06-13
# lesson 01
# task 5: Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма 
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки 
# (соотношение прибыли к выручке). 
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
print("simplest economic calculator")
gain = float(input("type gain/take value: ")) # need error handler
cost = float(input("type cost value: ")) # need error handler
margin = gain - cost
if margin < 0:
    print(f"financial result for the period depressing, all fired. Margin is {margin:.2f}$")
    raise SystemExit
efficiency = margin / gain
print(f"very good, your team got margin = {margin:.2f}$ efficiency is {efficiency:.2f}")
count_team = int(input("type count members of your team (don't forget about yourself): "))
mergin_per_team_member = margin / count_team
print(f"your results for that period\nmargin={margin:.2f}$\nefficiency={efficiency:.2f}\nmargin per team ({count_team} people with me) member={mergin_per_team_member:.2f}$")
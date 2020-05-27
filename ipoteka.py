ost_zadolz= float(input("введите остаток задолженности: "))
prots_in_day= (10.9/100)/366
daily_prots= ost_zadolz*prots_in_day 
date_pogash= 17 #дата погашения
date_today= int(input("введите сегодняшнее число: "))
u = "введите день от 1 числа до %s числа месяца" 
if date_today <1 or > date_pogash:
    print(u % date_pogash )
sum_of_prots_for_pay_day= daily_prots * (date_pogash - date_today)
sum_on_deposit= float(input("введите сумму на счете: "))
sum_for_pay= sum_on_deposit - sum_of_prots_for_pay_day
x = sum_of_prots_for_pay_day + sum_for_pay
print("сумма дорочного погашения", sum_for_pay) 
print("проценты в день погашения", sum_of_prots_for_pay_day)
print("общая сумма", x)
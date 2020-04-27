#!/usr/bin/env python3
basic_salary = 1500
bonus_rate = 200
comission_rate = 0.02
numberofcamera = int(input("请输入相机数量： "))
price = float(input("请输入单价: "))
bonus =（bonus_rate * numberofcamera）
commossion = (commission_rate * price * numberofcamera)
print("卖出得到的金额： {:6.2f}".format(bonus))
print("卖出获得的抽成： {:6.2f}".format(commossion))
print("总工资： {:6.2f}".format(basic_salary + bonus + commossion))


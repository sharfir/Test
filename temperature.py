#!/usr/bin/env python3
fahrenheit = 0
print("华氏温度 摄氏温度 ")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8  #将华氏转化为摄式度
    print("{:5d} {:7.2f}".format(fahrenheit, celsius))
    fahrenheit = fahrenheit + 25

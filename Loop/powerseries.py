#!/usr/bin/env python3
x = float(input("请输入x的值： "))
n = term = num = 1
result = 1.0
while n< 100:
    term *= x / n
    result += term
    n += 1
    if term < 0.0001:
        break
print("no of times= {} and sum= {}".format(n, result))


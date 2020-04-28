#!/usr/bin/env python3
#打印斐波那契数列，一行打印出来，print()的另一个参数end来替换这个换行符
a, b = 0, 1
while b < 100:
    print(b, end='  ')
    a, b = b, a+b
print()

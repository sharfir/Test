#!/usr/bin/env python3
#打印斐波那契数列，设置数列的前两项为1，之后的每一项都是前两项之和
a,b = 0,1
while b < 100:
    print(b)
    a, b = b, a+b

#!/usr/bin/env python3
#程序设置用户输入一个正整数，若是大于100，输出：您输入的数大于100，
#若是小于100，大于50 ，输出：你输入的数小于100，大于50
#若是输入的数小于50，输出：你输入的数小于50

number = int(input("请输入一个正整数： "))
if number > 100:
    print("你输入的数大于100")
elif number <100 and number > 50:
    print("你输入的数小于100，大于50")
elif number < 50:
    print("你输入的数小于50")
else:
    print("你输入的数是：{}".format(number))

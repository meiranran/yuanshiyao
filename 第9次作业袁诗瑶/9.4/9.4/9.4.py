import random as r

a=int(input("请输入最多能说的数字个数"))
b=int(input("请输入初始数"))
c=int(input("请输入获胜的数"))
#已a+1为一组
while(c>=b):
    c=c-(a+1)
print("获胜条件：能数到{}".format(c+(a+1)))

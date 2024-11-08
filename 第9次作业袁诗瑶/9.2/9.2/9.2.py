time=11
num=26625
print("第{}小时巨噬细胞有{}个".format(time,num))

for i in range(11):
    time=time-1
    num=(num-1)//2+1
    print("第{}小时巨噬细胞有{}个".format(time,num))

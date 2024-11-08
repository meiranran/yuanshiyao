time=0
num=27

while(num<=100000):
    time=time+1
    num=(num-1)*2+1

print("至少需要{}个小时".format(time+1))

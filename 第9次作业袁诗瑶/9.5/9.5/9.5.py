x=1
while(x==1):
    N=int(input("未来几年"))
    for i in range(0,N):
        a=2024+i
        if(a%4==0 and a%400!=0):
            print("{}年为普通闰年".format(a))
        elif(a%400==0):
            print("{}年为世纪闰年".format(a))
    x=int(input("是否再来一次，1:是的，2：不玩了"))
        

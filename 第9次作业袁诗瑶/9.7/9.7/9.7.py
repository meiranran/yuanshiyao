#{:^10d}  中间对齐，宽度为10
'''
ls=[1,2,3,4,5,6,7,8]
for i in range(len(ls)):
    print("{:^10}".format(ls[i]),end='')
'''
def pascal_date(n):
    date=[]
    for i in range(n):
        ls=[1]
        if(i>0):
            last_ls=date[i-1]
            for j in range(len(last_ls)-1):
                ls.append(last_ls[j]+last_ls[j+1])
            ls.append(1)
        date.append(ls)
    return date

n=int(input("行数"))
for ls in pascal_date(n):
    print("  "*(n-len(ls)),end='')
    for num in ls:
        print(num,end='   ')
    print()

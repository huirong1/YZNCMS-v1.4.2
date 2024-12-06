def add(x,y):
    #加法运算
    return x+y

def subtract(x,y):
    #减法运算
    return x-y
def multiply(x,y):
    #乘法运算
    return x*y

def divide(x,y):
    #除法运算
    if y==0:
        return "除数不能为0"
    else:
        return x/y

while True:
    print("请选择运算：")
    print("1、相加")
    print("2、相减")
    print("3、相乘")
    print("4、相除")
    print("5、退出")
    choice=input("请输入你的选择（1/2/3/4/5）：")
    if choice in ('1','2','3','4'): 
        num1=float(input("请输入第一个数字："))
        num2=float(input("请输入第二个数字："))
        if choice=='1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice=='2':
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice=='3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice=='4':
            print(num1,"/",num2,"=",divide(num1,num2))
    elif choice=='5':
        print("退出")
        break
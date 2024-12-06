import random

def guess_number():
    number = random.randint(1, 100)
    guess = 0
    da= []
    i=0
    while guess != number:
        guess = int(input("猜一个1到100之间的数字："))
        da.append(guess)
        i+=1
        if guess < number:
            print("太小了！")
        elif guess > number:
            print("太大了！")
    print("恭喜你，猜对了！答案是%d", number)
    print("你一共猜了%d次" % i)
    print("你猜的数字分别是：",da)

if __name__ == "__main__":
    guess_number()
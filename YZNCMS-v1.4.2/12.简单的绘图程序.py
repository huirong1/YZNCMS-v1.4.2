import turtle

def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def draw_spiral():
    turtle.width(2)  # 画笔宽度
    for _ in range(36):
        turtle.forward(_ * 3)
        turtle.right(45)

def main():
    turtle.speed(10)  # 设置绘制速度
    draw_square()
    turtle.penup()  # 抬起画笔
    turtle.goto(-50, -50)  # 移动到新位置
    turtle.pendown()  # 放下画笔
    draw_spiral()
    print("123")
    turtle.done()  # 结束绘图
    print("绘制完成！")
if __name__ == "__main__":
    main()
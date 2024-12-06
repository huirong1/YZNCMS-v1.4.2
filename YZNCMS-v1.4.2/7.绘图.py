import turtle

def draw_square():
    """使用turtle绘制正方形"""
    
    # turtle.width(2)  # 画笔宽度
    for i in range(300):
        turtle.forward(5+i*5)  # 向前移动
        turtle.right(145)     # 右转90度
        # turtle.right(144)     # 右转144度
# 144五角星
    # turtle.right(45)     # 右转90度
    # turtle.forward(600)  # 向前移动
def main():
    turtle.speed(50)  # 设置绘制速度
    draw_square()    # 绘制正方形
    turtle.done()    # 结束绘制
    # turtle.bye()      # 关闭窗口


if __name__ == "__main__":
    main()    
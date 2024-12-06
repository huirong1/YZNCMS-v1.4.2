import turtle

def main():
    # 设置画布
    screen = turtle.Screen()
    screen.title("使用鼠标画画")
    screen.setup(width=600, height=600)
    
    # 创建一个turtle对象
    painter = turtle.Turtle()
    painter.speed(0)  # 最快速度
    painter.width(2)  # 画笔宽度

    # 鼠标点击事件处理，用于设置起始点
    def mouse_click(x, y):
        painter.pendown()  # 放下画笔准备画
        painter.goto(x, y)  # 移动到鼠标点击的位置

    # 鼠标点击事件处理，判断是否为右键点击以关闭程序
    def close_program(x, y):
        screen.bye()  # 关闭画布

    # 绑定鼠标点击事件和判断右键关闭程序
    screen.onclick(mouse_click)  # 鼠标左键点击事件
    screen.onclick(close_program, btn=3)  # 鼠标右键点击事件，关闭程序

    screen.mainloop()

if __name__ == "__main__":
    main()

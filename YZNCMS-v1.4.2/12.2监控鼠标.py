from pynput.mouse import Listener as MouseListener, Button
from pynput.keyboard import Listener as KeyboardListener, Key

# 标记是否正在监听鼠标
is_listening = False

# 监控鼠标位置变化
def on_move(x, y):
    if is_listening:
        print('鼠标移动到 ({0}, {1})'.format(x, y))

# 监控鼠标按键事件
def on_click(x, y, button, pressed):
    global is_listening
    if button == Button.left and pressed:
        if is_listening:
            is_listening = False
            print("停止监听鼠标位置")
        else:
            is_listening = True
            print("开始监听鼠标位置")

# 监控键盘按键事件
def on_press(key):
    if key == Key.esc:
        return False

# 启动鼠标监听和键盘监听
mouse_listener = MouseListener(on_move=on_move, on_click=on_click)
keyboard_listener = KeyboardListener(on_press=on_press)

with mouse_listener, keyboard_listener:
    mouse_listener.join()
    keyboard_listener.join()

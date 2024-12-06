import datetime

# 事件存储文件
EVENTS_FILE = 'events.txt'

def display_current_date():
    now = datetime.datetime.now()
    print(f"当前日期：{now.strftime('%Y-%m-%d')}")

def add_event():
    event_date = input("请输入事件日期 (格式：YYYY-MM-DD)：")
    if event_date.__len__() != 10 or event_date[4] != '-' or event_date[7] != '-':
        print("无效的日期格式，请重新输入。")
        return
    event_description = input("请输入事件描述：")
    event = f"{event_date}\t{event_description}\n"
    with open(EVENTS_FILE, 'a') as file:
        file.write(event)
    print("事件已添加。")

def load_events():
    try:
        with open(EVENTS_FILE, 'r') as file:
            events = file.readlines()
        events = [event.strip() for event in events if event.strip()]
        return events
    except FileNotFoundError:
        return []

def save_events(events):
    with open(EVENTS_FILE, 'w') as file:
        for event in events:
            file.write(event + '\n')

def view_events():
    events = load_events()
    if not events:
        print("没有事件。")
    else:
        for i, event in enumerate(events):
            print(f"{i + 1}. {event}")

def main():
    print("欢迎来到简易日历应用")
    while True:
        display_current_date()
        user_input = input("输入 '1' 来添加事件，'2' 来查看事件，或输入 '0' 来退出：")
        if user_input == "1":
            add_event()
        elif user_input == "2":
            view_events()
        elif user_input == "0":
            print("感谢使用简易日历应用")
            break
        else:
            print("无效的输入，请重新输入。")

if __name__ == "__main__":
    main()
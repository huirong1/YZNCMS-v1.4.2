class Todolist:
    def __init__(self):
        self.todo_list = []

    def add_task(self, task):
        self.todo_list.append(task)
        print(f"任务 {task} 已添加到待办事项列表中。")
    
    def remove_task(self, task):
        try:
            self.todo_list.pop(task - 1)
            print(f"任务 {task} 已从待办事项列表中移除。")
        except IndexError:
            print("无效的任务id，请重新输入。")
        
    def view_tasks(self):
        if len(self.todo_list) == 0:
            print("待办事项列表为空。")
        else:
            print("待办事项列表：")
            for i, task in enumerate(self.todo_list, 1):
                print(f"{i}. {task}")


def main():
    todo = Todolist()
    while True:
        print("\n请选择操作：")
        print("1. 添加任务")
        print("2. 移除任务")
        print("3. 查看任务")
        print("4. 退出")
        choice = input("请输入选项：")

        if choice == "1":
            task = input("请输入要添加的任务：")
            todo.add_task(task)
        elif choice == "2":
            task = int(input("请输入要移除的任务id："))
            todo.remove_task(task)
        elif choice == "3":
            todo.view_tasks()
        elif choice == "4":
            print("退出程序。")
            break
        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    main()
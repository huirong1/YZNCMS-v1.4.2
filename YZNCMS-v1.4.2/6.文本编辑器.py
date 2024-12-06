def create_file(file_name):
    """创建一个新文件并返回文件对象"""
    with open(file_name, 'w') as file:
        pass
    return open_file(file_name)

def open_file(file_name):
    """打开一个已存在的文件并返回文件对象"""
    try:
        return open(file_name, 'a+')
    except FileNotFoundError:
        print("文件不存在。")
        return None

def write_to_file(file, text):
    """将文本写入文件"""
    file.write(text)
    file.seek(0)  # 回到文件开头以便读取

def read_file(file):
    """读取文件内容"""
    file.seek(0)  # 回到文件开头
    return file.read()

def main():
    file_name = input("请输入文件名（新文件或已存在的文件）：")
    file = create_file(file_name) if file_name else open_file(file_name)
    
    if file:
        while True:
            print("\n文本编辑器 - 命令：")
            print("1. 写入文本")
            print("2. 读取文本")
            print("3. 保存并退出")
            command = input("请输入命令：")
            
            if command == '1':
                text = input("请输入要写入的文本：\n")
                write_to_file(file, text)
                print("文本已写入。\n")
                
            elif command == '2':
                content = read_file(file)
                print("文件内容：\n", content)
                
            elif command == '3':
                file.close()
                print("文件已保存并退出。")
                break
            else:
                print("无效的命令。")

if __name__ == "__main__":
    main()
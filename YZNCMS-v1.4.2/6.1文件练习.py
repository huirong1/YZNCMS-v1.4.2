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

def files():
    file_name='123.txt'
    file = create_file(file_name) if file_name else open_file(file_name)
    return file

if __name__ == '__main__':
    file = files()
    print(file.read())
    file.close()
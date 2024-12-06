import random
import string

def generate_password(length):
    """生成一个随机密码"""
    if length < 4:
        print("密码长度至少为4，请重新输入。")
        return None

    # 可能的密码字符集合
    characters = string.ascii_letters + string.digits + string.punctuation

    # 确保密码中至少包含一个小写字母、一个大写字母、一个数字和一个特殊字符
    password = [
        # random.choice(string.ascii_lowercase),# 小写字母
        # random.choice(string.ascii_uppercase),# 大写字母
        # random.choice(string.digits),# 数字
        # random.choice(string.punctuation),# 特殊字符
    ]

    # 填充剩余的密码长度
    for _ in range(length):
        password.append(random.choice(characters))

    # 打乱密码列表以避免模式
    # random.shuffle(password)

    # 将列表转换为字符串
    return ''.join(password)

def main():
    password_length = int(input("请输入想要的密码长度（至少4位）："))
    password = generate_password(password_length)
    if password:
        print("生成的密码是：", password)

if __name__ == "__main__":
    main()
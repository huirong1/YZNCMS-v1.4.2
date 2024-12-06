def chat_bot():
    print("你好！我是你的聊天机器人。")
    print("输入'退出'来结束对话。")

    while True:
        user_input = input("你：")
        if user_input == "退出":
            print("聊天机器人：再见！")
            break

        # 简单的回应逻辑
        if "你好" in user_input:
            print("聊天机器人：你好！很高兴和你聊天。")
        elif "你是谁" in user_input:
            print("聊天机器人：我是一个简单的聊天机器人。")
        elif "谢谢" in user_input:
            print("聊天机器人：不客气！")
        else:
            print("聊天机器人：对不起，我不太明白你的意思。")

if __name__ == "__main__":
    chat_bot()
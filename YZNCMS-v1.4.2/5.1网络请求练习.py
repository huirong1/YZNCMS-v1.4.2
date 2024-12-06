import requests  # 导入requests库
import time  # 导入time库

if __name__ == '__main__':
    # 构建带有当前时间戳的URL
    url = f"http://localhost:8081/hello?a1={time.time()}"
    for i in range(10):
        response = requests.get(url)
        print(response.text)
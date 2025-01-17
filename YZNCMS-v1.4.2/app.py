from flask import Flask, request
import time

app = Flask(__name__)

def testdata():
    filename = '1.txt'
    # 以追加模式打开文件，这样每次调用函数时都会在文件末尾追加内容
    with open(filename, 'a') as handle:
        # 获取当前时间戳
        time_now = int(time.time())
        # 获取请求方法（GET或POST）
        method = request.method
        # 获取请求的URL
        url = request.path
        # 获取客户端IP地址
        ip = request.remote_addr

        # 构造要写入文件的内容
        log_entry = f"Time: {time_now}\nMethod: {method}\nURL: {url}\nIP: {ip}\n\n"

        # 写入请求信息
        handle.write(log_entry)

    # 输出记录内容
    print(log_entry)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
def index():
    testdata()
    return "Request logged!"

if __name__ == '__main__':
    # 启动Flask应用，监听所有IP地址的8080端口
    app.run(port=8080,debug=True)
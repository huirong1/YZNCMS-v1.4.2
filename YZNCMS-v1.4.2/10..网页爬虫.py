import requests
from bs4 import BeautifulSoup

def simple_web_crawler(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        # 指定编码为UTF-8
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title').text
        print(f"网页标题：{title}")
        # print("网页内容："+response.text)
    except requests.RequestException as e:
        print(f"请求错误：{e}")
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    url = "http://localhost:8081/Files.html"  # 替换为你想爬取的网页地址
    # url = "http://localhost:8081/hello"  # 替换为你想爬取的网页地址
    simple_web_crawler(url)
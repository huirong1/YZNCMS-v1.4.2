# 导入requests库来获取最新的汇率数据
import requests

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    
    if to_currency in data['rates']:
        return data['rates'][to_currency]
    else:
        return None

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is not None:
        return amount * rate
    else:
        return "Currency not supported."

def main():
    sum = input("输入1查看货币代码及其对应的中文名称，输入其他任意键开始转换：")
    if sum == "1":
        print_currencies()
    
    print("货币转换器")
    amount = float(input("请输入金额："))
    from_currency = input("请输入源货币类型（如USD）：")
    to_currency = input("请输入目标货币类型（如EUR）：")
    
    result = convert_currency(amount, from_currency, to_currency)
    
    if isinstance(result, float):
        print(f"{amount} {from_currency} 等于 {result:.2f} {to_currency}")
    else:
        print(result)
# 货币代码到中文名称的映射字典
currency_dict = {
    "CNY": "人民币",
    "USD": "美元",
    "EUR": "欧元",
    "JPY": "日元",
    "GBP": "英镑",
    "AUD": "澳大利亚元",
    "CAD": "加拿大元",
    "CHF": "瑞士法郎",
    "SEK": "瑞典克朗",
    "NZD": "新西兰元",
    "KRW": "韩元",
    "INR": "印度卢比",
    "BRL": "巴西雷亚尔",
    "RUB": "俄罗斯卢布",
    "MXN": "墨西哥比索",
}

def print_currencies():
    # 打印所有货币代码及其对应的中文名称
    print("货币代码及其对应的中文名称：")
    for code, name in currency_dict.items():
        print(f"{code}: {name}")

# 调用函数打印货币信息
#print_currencies()

if __name__ == "__main__":
    main()
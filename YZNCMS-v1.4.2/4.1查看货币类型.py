import requests

def get_supported_currencies():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return list(data['rates'].keys())

def main():
    supported_currencies = get_supported_currencies()
    print("支持的货币类型：")
    for currency in supported_currencies:
        print(currency)

if __name__ == "__main__":
    main()
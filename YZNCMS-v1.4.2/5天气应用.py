import requests

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=fc7f7ec5ce0584255ad558d7bd7cfdcc&units=metric"
    response = requests.get(url)
    return response.json()

def main():
    # api_key = input("请输入你的OpenWeatherMap API密钥：")
    city = input("请输入你想要查询的城市：")

    weather_data = get_weather(city)
    
    if weather_data['cod'] == 200:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        print(f"{city} 的天气：")
        print(f"温度：{temperature}°C")
        print(f"描述：{description}")
    else:
        print(weather_data)
        print("无法获取天气信息，请检查城市名称和API密钥。")

if __name__ == "__main__":
    main()
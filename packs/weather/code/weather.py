import requests
import sys
from libabr import *
files = Files()
colors = Colors()
# func
Api_Key = "6f3b33e8218c2f0a443e3d8db121bb68"

if sys.argv[1:]==[]:
    CityName = input('Enter your city name: ').lower()
else:
    CityName = sys.argv[1]

Url = f"https://api.openweathermap.org/data/2.5/weather?q={CityName}&appid={Api_Key}"
result = requests.get(Url)
data = result.json()
if data["cod"] == "404":
    colors.show('weather','fail',"Something wrong!")
else:
    # گرفتن اطلاعات
    main = data["main"]
    # گرفتن دما
    pre_temp = main["temp"]
    temp = pre_temp - 275.15
    temp = round(temp)
    # گرفتن فشار
    pressure = main["pressure"]
    # رطوبت هوا
    humidity = main["humidity"]
    # توضیحات
    weather = data["weather"]
    description = weather[0]["description"]
    print("Temperature (k):",int(pre_temp))
    print("Temperature (C):",temp)
    print("Temperature (F):",str(int(int(temp)*9/5+32))) # http://banbaey.blogfa.com/post/690
    print("Air pressure:",pressure)
    print("Humidity:",humidity)
    print("Description:",description)

    files.write('/etc/location/city', CityName)
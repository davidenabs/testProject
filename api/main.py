import requests
import datetime

#
apiKey = '4e8216210776efff56260323227888f5'

city = input('Enter your city: ')

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Temperature: {data['main']['temp']}")
    print(f"Humidity: {data['main']['humidity']}")

    # forcast
    lon = data['coord']['lon']
    lat = data['coord']['lat']
    print('Forcast')
    url_end_point = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apiKey}&units=metric"

    xresponse = requests.get(url_end_point)

    if xresponse.status_code == 200:
        xdata = xresponse.json()

        for i in xdata['list']:
            dt = datetime.datetime.fromtimestamp(i['dt']).strftime('%Y-%m-%d %H:%M:%S')
            print(f"Time: {dt}")
            print(f"\t Temp: {i['main']['temp']}")
            print(f"\t Hum: {i['main']['humidity']}")
            print('--------')

    else:
        print(xresponse.status_code)
        print('Unable to get forcast')
else:
    print('Something went wrong here!')


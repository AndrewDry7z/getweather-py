import json
import urllib.request

# get city name
ipApiResponse = urllib.request.urlopen('http://ip-api.com/json/').read().decode('utf8')
jsonDataIp = json.loads(ipApiResponse)
cityName = jsonDataIp['city']
print(cityName)

# get the weather
appID = 'xxx' # !!! get your own ID here: https://openweathermap.org/api
apiURL = 'http://api.openweathermap.org/data/2.5/weather?q=' + cityName + '&APPID=' + appID + '&units=metric'


def get_weather():
    weather_api_response = urllib.request.urlopen(apiURL).read().decode(
        'utf8')
    json_data_weather = json.loads(weather_api_response)
    temperature_value = int(json_data_weather['main']['temp'])
    print(str(temperature_value) + '° C')


try:
    get_weather()
except 'urllib.error.HTTPError':
    print('err')

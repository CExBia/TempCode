#enconding utf-8
import requests
import json
city_name = 'São Paulo'

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&APPID=18db156f5ef1c6bdad1be1c5072fa282')
r2 = r.json()
r3 = json.dumps(r2)
temp = float(r2['main']['temp']) - 273.15
temp_int = int(temp)

print(str(temp_int)+' '+'Graus Celsius')

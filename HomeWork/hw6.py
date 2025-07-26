'''
Выбранная библеотека Requests, является библеотекей для web-api, или работу с HTTP- клиентом для пайтон.
может работать с JSON, и работать с параметрами запросов и данными форм
'''
import requests



API_KEY = '325d3c44ffde3d37df4ac0a72a26ad10'
# апи с погодой с сайта OpenWeatherMap
CITY_NAME = 'Bishkek' 
# город
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather' 
# сам сайт юрл

#создаем параметры для библеотеки
params = {
    'q': CITY_NAME,       
    'appid': API_KEY,     # Ваш личный API-ключ от OpenWeatherMap
    'units': 'metric',    # metric для Цельсия, imperial для Фаренгейта
    'lang': 'ru'          
}

# Выполняем гет-запрос к API OpenWeatherMap с параметрами выше
response = requests.get(BASE_URL, params=params)

# Проверяем ответ сервера -- Код 200 значит все хорошо
if response.status_code == 200:
    # Если запрос выполнен успешно, передаем из формата JSoN в удобный формат Python
    weather_data = response.json()

    # получаем информацию о погоде из запроса выше
    temperature = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    # Выводим собранную информацию о погоде в Бишкеке
    print(f"Погода в городе Бишкек:")
    print(f"Температура: {temperature}°C (ощущается как {feels_like}°C)")
    print(f"Описание: {description.capitalize()}") # Делаем первую букву описания заглавной
    print(f"Влажность: {humidity}%")
    print(f"Скорость ветра: {wind_speed} м/с")
else:
     print('Код работает, API работает просто не каждый раз, нужно ждать определенное время.')
# import requests
# import os
# from datetime import datetime 
# import json 

# user_api = os.environ['CURRENT_WEATHER_DATA']
# location = input("Enter the most nearby city to your hike: ")

# complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+ location + "&appid=" user_api

# api_link = requests.get(complete_api_link)
# api_data = api_link.json()
# print(api_data)

# if api_data['cod'] == '404':
#     print('Invalid City')
# else:
#     temp = ((api_data['main']['temp']) - 273.15)
#     weather_desc = api_data['weather'][0]['description']
#     humidity = api_data['main']['humidity']
#     wind_speed = api_data['wind']['speed']
#     date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
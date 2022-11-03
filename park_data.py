import json
import requests
import os


API_Key_NPS = 'N4oee4Qy9v9duGaBEhJoxvvDa66aeMKp9aNAZUJr'
endpoint = "https://developer.nps.gov/api/v1/parks?"
parameters = {
    "api_key": API_Key_NPS,
    "q":'hiking',
    'limit': '275',
    'start': '1'
} 
response = requests.get(endpoint, params=parameters)
data_all = response.json()
list_of_parks = data_all['data']
seedlist = []
photolist = []
hikepk = 2
photopk = 1
for park in list_of_parks: # iterate over all information about the first park in the list
#     seed_file = open("seed.json", "a")

    elevation_endpoint = "https://nationalmap.gov/epqs/pqs.php?"
    elevation_params = {
        "x":  park['longitude'],
        "y": park['latitude'],
        "units": 'feet',
        "output": 'json'
    } 
    res = requests.get(elevation_endpoint, params=elevation_params)
    res = res.json()
    altitude = res['USGS_Elevation_Point_Query_Service']['Elevation_Query']['Elevation']
    altitude = float(altitude)
    if altitude > (-100):
        difficulty = ''
        if altitude <= 3000:
            difficulty = 'E'
        elif altitude > 3000 and altitude < 6000: 
            difficulty = 'M'
        else:
            difficulty = 'D'
        park['altitude'] = altitude

        obj = park['addresses'][0]
        test = obj['line1'] + '\n' + obj['city'] + ', ' + obj['stateCode'] + ' ' + obj['postalCode']

        outputobj = {
            "model": "main_app.hike",
            'fields': {
                'user': 1,
                'name': park['fullName'],
                'difficulty': difficulty,
                'description': park['description'],
                'location': test,
                'altitude': park['altitude'],
                'directions': park['directionsUrl']
            }
        }
        
        
        seedlist.append(outputobj)
        for img in park['images']:
            outputphoto = {
                "model": "main_app.photo",
                'fields': {
                    'user': 1,
                    'hike': hikepk,
                    'url': img['url']
                }
            }
            photolist.append(outputphoto)
            photopk+=1
        hikepk += 1
thing = {

}

with open('0002_seed.json', 'w') as fp:
    json.dump(seedlist, fp)
with open('0003_seed.json', 'w') as fp:
    json.dump(photolist, fp)


# fullName, addresses, images, altitude, directionsUrl

# [
#     {
#         "model": "admin_birpen.admin",
#         "pk": 1,
#         "fields": {
#           "username": "@admin"
#         }
#     },
# ]
import requests
# Replace 'YOUR_API_KEY' with your actual OpenCage API key
API_KEY = 'c59d1124652340dea253de6cf72a6c3f'

# The location you want to geocode
location = 'kisumu, Kenya'

# Create the API request URL
base_url = 'https://api.opencagedata.com/geocode/v1/json'
params = {
    'q': location,
    'key': API_KEY
}

# Send the request to the OpenCage API
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    if data['status']['code'] == 200:
        # Extract the latitude and longitude from the response
        latitude = data['results'][0]['geometry']['lat']
        longitude = data['results'][0]['geometry']['lng']

        print(f'Location: {location}')
        print(f'Latitude: {latitude}')
        print(f'Longitude: {longitude}')
    else:
        print(f'Error: {data["status"]["message"]}')
else:
    print(f'HTTP Error: {response.status_code}')

import requests

# Replace 'YOUR_API_KEY' with your actual OpenCage API key
API_KEY = 'b41d417937094665ab100b905a07fea6'

# The location you want to geocode
location = 'Nairobi Kenya'

# Create the API request URL
base_url = 'https://api.opencagedata.com/geocode/v1/json'
params = {
    'q': location,
    'key': API_KEY
}

# Send the request to the OpenCage API
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    if data['status']['code'] == 200:
        # Extract the latitude and longitude from the response
        latitude = data['results'][0]['geometry']['lat']
        longitude = data['results'][0]['geometry']['lng']

        print(f'Location: {location}')
        print(f'Latitude: {latitude}')
        print(f'Longitude: {longitude}')
    else:
        print(f'Error: {data["status"]["message"]}')
else:
    print(f'HTTP Error: {response.status_code}')


import requests
import json
import os

api_url = 'https://randomuser.me/api/'

response = requests.get(api_url)

if response.status_code == 200:
    new_user = response.json()['results'][0]

    # Read existing data from the file
    if os.path.exists('data.json'):
        with open('data.json', 'r') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    # Append the new user data
    existing_data.append(new_user)

    # Write the updated data back to the file
    with open('data.json', 'w') as file:
        json.dump(existing_data, file, indent=2)
    print('Data successfully appended to data.json')
else:
    print('Error fetching data from API:', response.status_code)

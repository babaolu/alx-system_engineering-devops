#!/usr/bin/python3
import requests

# Set up your Datadog API credentials
api_key = '558be1bca5a6471ec9f5ce4c4aa8845c'
app_key = '28c3c86bebf85fdcaae42808d31efce4f847867e'

# Define the URL for the Dashboards API endpoint
url = 'https://api.datadoghq.com/api/v1/dashboard'

# Set up the headers with your API and APP keys
headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key
}

# Make a GET request to the Dashboards API endpoint
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON
    dashboards = response.json()['dashboards']
    
    # Iterate over the dashboards and print their IDs
    for dashboard in dashboards:
        print("Dashboard ID:", dashboard['id'])
else:
    print("Error:", response.status_code)

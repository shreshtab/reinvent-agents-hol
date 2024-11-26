import os
import requests
import json

def get_top_offers(customer_id: str):
    # Define the API endpoint and parameters
    api_url = f'https://example.com/api/customers/{customer_id}'  # Replace with the actual API URL
    response = requests.get(api_url)
    
    # Get Env Variables
    AWS_NEPTUNE_ENDPOINT = os.getenv('AWS_NEPTUNE_ENDPOINT')
    AWS_NEPTUNE_ENDPOINT_PORT = os.getenv('AWS_NEPTUNE_ENDPOINT_PORT')

    # # Check if the request was successful
    # if response.status_code == 200:
    #     # Return the response as an array of strings (assuming the API returns a list of strings)
    #     return response.json()  # Assumes the response is a JSON array of strings
    # else:
    #     # Handle error if the request fails
    #     print(f"Error: Unable to fetch data for Customer ID {customer_id}, Status Code: {response.status_code}")
    #     return []

    print(customer_id)

    return ["Flat Screen TV", "Ninja Creami", "Playstation 5"]
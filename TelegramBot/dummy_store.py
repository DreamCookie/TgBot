import requests

def get_products():
    url = "https://dummyjson.com/products"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return "Error: Unable to fetch products"

# You can add more functions here to interact with different endpoints of the API

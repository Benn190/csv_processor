import requests
import pandas as pd

# makeup api provides data on many makeup items. Including details such as product type, price, and available colours.
def get_makeup_data():
    # define API endpoint URL
    endpoint = "https://makeup-api.herokuapp.com/api/v1/products.json"
    
    try:
        # make request
        print("Making API request")
        response = requests.get(endpoint)
        
        # check if request was successful (200 OK status code)
        if response.status_code == 200:
            print("Request successful")
            makeup_items = response.json()
            return makeup_items
        else:
            print("Error: ", response.status_code)
    
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        
def main():

    posts = get_makeup_data()
    
    if posts:
        df = pd.json_normalize(posts)
        df.to_csv('data/raw/makeup.csv', encoding='utf-8', index=False)
        print("Makeup data written to CSV")

if __name__ == '__main__':
    main()
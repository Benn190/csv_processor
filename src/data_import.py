import requests
import pandas as pd
import time
import json

# makeup api provides data on many makeup items. Including details such as product type, price, and available colours.
def get_makeup_data():
    # define API endpoint URL
    endpoint = "https://makeup-api.herokuapp.com/api/v1/products.json"
    
    try:
        # make request
        #print(time.strftime('%l:%M%p %Z on %b %d, %Y'))
        print(time.strftime('%x %X') + " - Making API request")
        response = requests.get(endpoint)
        
        # check if request was successful (200 OK status code)
        if response.status_code == 200:
            print(time.strftime('%x %X') + " - Request successful, status code: " + str(response.status_code))
            makeup_items = response.json()
            return makeup_items
        else:
            print(time.strftime('%x %X') + " - Error: ", response.status_code)
    
    except requests.exceptions.RequestException as e:
        print(time.strftime('%x %X') + " - Error: ", e)
        
def main():

    posts = get_makeup_data()
    
    if posts:
        
        print(time.strftime('%x %X') + " - Writing JSON Makeup data to .json file")
        with open('data/raw/makeup.json', 'w') as f:
            json.dump(posts, f)
        
        # format json from API as a pandas dataframe
        df = pd.json_normalize(posts)
        print(time.strftime('%x %X') + " - Converting API JSON response to pandas dataframe")
        
        # convert dataframe and save as csv
        df.to_csv('data/raw/makeup.csv', encoding='utf-8', index=False)
        print(time.strftime('%x %X') + " - Makeup data written to CSV")

if __name__ == '__main__':
    main()
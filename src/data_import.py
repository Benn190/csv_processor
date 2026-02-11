import requests
import pandas as pd
import time
import os 
import shutil

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
     
def clear_raw_data():
    dir = "data/raw"
    files = os.listdir(dir)
    for f in files:
        f_path = os.path.join(dir, f)
        if os.path.isfile(f_path):
            os.remove(f_path)
        
def main():

    print(time.strftime('%x %X') + " - Removing existing data from data/raw")
    clear_raw_data()

    makeup_data = get_makeup_data()
    
    if makeup_data:
        
        # format json from API as a pandas dataframe
        df = pd.json_normalize(makeup_data)
        print(time.strftime('%x %X') + " - Converting API JSON response to pandas dataframe")
        
        file_path = "data/raw/makeup.csv"
        
        # convert dataframe and save as csv
        df.to_csv(file_path, encoding="utf-8", index=False)
        print(time.strftime('%x %X') + " - Makeup data written to CSV: " + file_path)
        
    else:
        print(time.strftime('%x %X') + " - Error: No makeup data found")

if __name__ == '__main__':
    main()
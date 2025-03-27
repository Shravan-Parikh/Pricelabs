import csv
from api_client import build_headers, build_search_body, fetch_from_api

API_URL = 'https://www.booking.com/dml/graphql'

def get_properties(address, page_size, lat=None, lng=None):
    #Main function to fetch property listings
    if not isinstance(address, str):
        raise ValueError('Please provide a valid text location')
    if (lat or lng) and not (isinstance(lat, float) and isinstance(lng, float)):
        raise ValueError('Coordinates must be float values')
    
    headers = build_headers()
    checkIn = '2025-03-29'
    checkOut = '2025-03-30'
    payload = build_search_body(address, page_size, checkIn, checkOut,lat, lng)
    
    data = fetch_from_api(API_URL, headers, payload)
    return extract_listing_data(data)

def extract_listing_data(api_response):
    #Extracts and formats listing data from API response
    results = api_response.get('data', {}).get('searchQueries', {}).get('search', {}).get('results', [])

    listings = []
    for result in results:
        # Get basic property info with default empty dict
        prop_data = result.get('basicPropertyData', {}) or {}
        
        # Get pricing information with default empty dicts
        price_info = result.get('priceDisplayInfoIrene', {}) or {}
        display_price = price_info.get('displayPrice', {}) or {}
        amount_per_stay = display_price.get('amountPerStay', {}) or {}
        display_name = result.get('displayName', {}) or {}
        
        listings.append([
            prop_data.get('id', 'N/A'),  # Default to 'N/A' if ID is missing
            display_name.get('text', 'N/A'),  
            prop_data.get('pageName', 'N/A'), 
            amount_per_stay.get('amount', 'N/A'),  
        ])
    
    return listings 

def save_to_csv(listings, filename='listings.csv'):

    #Saves listings data to CSV with specified headers
    headers = [
        'Listing ID', 
        'Listing Title', 
        'Page Name', 
        'Amount Per Stay'
    ]
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(listings)
        print(f'Successfully saved {len(listings)} properties to {filename}')
    except IOError as e:
        print(f'Error saving file: {e}')
    except Exception as e:
        print(f'Unexpected error occurred: {e}')
        

if __name__ == "__main__":
    try:
        # Example usage with coordinates

        #data = get_properties('Bangalore', 20, 12.9716, 77.5946) # with coordinates
        
        # Example usage without coordinates
        
        data = get_properties('Dubai', 30) 
        
        save_to_csv(data)

    except Exception as e:
        print(f"Error occurred: {str(e)}")
import requests
import json
import config
import time

KEY = config.API_KEY

def google_geocoding(address):
    """get the coordinates of an address
    
    Args:
        address (str): the address

    
    Returns:
        dict: return dict of latitude and longitude
    """
    
    geocodeing_api = f"https://maps.googleapis.com/maps/api/geocode/json?key={KEY}&address={address}"

    geocoding = json.loads(requests.get(geocodeing_api).text)
    lat = geocoding["results"][0]["geometry"]["location"]["lat"]
    lng = geocoding["results"][0]["geometry"]["location"]["lng"]

    return {"latitude": lat, "longitude": lng}

def google_nearbysearch(latitude, longitude, establishment, radius_in_meter=1000):
    """get the list of establishments within a radius for a pair of lat-lon
    
    Args:
        latitude (str): the latitude of the place
        longitude (str): the longitude of the place
        establishment (str): the type of establishment, such as school and supermarket
        radius_in_meter (int): search radius in meter

    
    Returns:
        list: return a list of establishments
    """

    query = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={KEY}&type={establishment}&location={latitude},{longitude}&radius={radius_in_meter}"

    result = json.loads(requests.get(query).text)
    
    final_list = []
    
    for hit in result["results"]:
       final_list.append(hit["name"])
    

    while "next_page_token" in result:
        time.sleep(2)
        query = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={KEY}&pagetoken={result['next_page_token']}"
        
        result = json.loads(requests.get(query).text)
        
        for hit in result["results"]:
            final_list.append(hit["name"])

    return final_list


def driving_time_and_distance(ori, dest):
    """get the dict of distance between two places
    
    Args:
        ori (str): Place A
        dest (str): Place B

    
    Returns:
        dict: return a dict of distance description
    """

    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?key={KEY}&origins={ori}&destinations={dest}&mode=driving&language=en-EN&sensor=false"
    result= json.loads(requests.get(url).text)


    return {"distance_value": result["rows"][0]["elements"][0]["distance"]["value"], "distance_text": result["rows"][0]["elements"][0]["distance"]["text"], "duration_text": result["rows"][0]["elements"][0]["duration"]["text"], "duration_value": result["rows"][0]["elements"][0]["duration"]["value"]}
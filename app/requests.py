
from . import main
import urllib.request,json
from .models import Rover


api_key = None

base_url = None

photos_url = None


def configure_request(app):
    global api_key,base_url,photos_url
    api_key = app.config['ROVER_API_KEY']
    base_url = app.config['ROVER_API_SOURCES_URL']

def get_photos():
    '''
    Function that gets the json response to our url request
    '''
    get_photos_url = base_url.format(api_key)

    with urllib.request.urlopen(get_photos_url) as url:
        get_photos_data = url.read()
        get_photos_response = json.loads(get_photos_data)

        photos_results = None

        if get_photos_response['photos']:
            photos_results_list = get_photos_response['photos']
            photos_results = process_results(photos_results_list)


    return photos_results



def process_results(photos_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        photos_list: A list of dictionaries that contain photos details

    Returns :
        photos_results: A list of photos objects
    '''
    photos_results = []
    for photo_item in photos_list:
        photo = photo_item.get('id')
      
        
        photos_object = Rover(photo,name,date)
        photos_results.append(photos_object)
        
    return photos_results    

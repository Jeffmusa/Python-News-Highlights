from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting base url
base_url = app.config["NEWS_API_SOURCES_URL"]


def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results



def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        source = news_item.get('name')
        link = news_item.get('url')
        country = news_item.get('country')
        id = news_item.get('id')
        description = news_item.get('description')
        
        news_object = News(source,link,country,id,description)
        news_results.append(news_object)
        
    return news_results    
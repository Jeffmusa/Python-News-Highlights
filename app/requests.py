# from app import app
from . import main
import urllib.request,json
from .models import News,Articles

# News = news.News
# Articles = news.Articles

# # Getting api key
# api_key = app.config['NEWS_API_KEY']

# #Getting base url
# base_url = app.config["NEWS_API_SOURCES_URL"]

# articles_url = app.config["HEADLINES_URL"]

api_key = None

base_url = None

articles_url = None


def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_SOURCES_URL']
    articles_url = app.config['HEADLINES_URL']

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




def get_articles(id):
    get_articles_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        print(get_articles_response)
        articles_results = None


        if get_articles_response["articles"]:
            articles_results_list = get_articles_response["articles"]
            articles_results = process_articles(articles_results_list)


    return articles_results



def process_articles(articles_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    articles_results = []
    for articles_item in articles_list:
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        poster = articles_item.get('urlToImage')
        time = articles_item.get('publishedAt')
        
        articles_object = Articles(author,title,description,url,poster,time)
        articles_results.append(articles_object)
        
    return articles_results    

from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    #getting news
    news = get_news()
    print(news)
    title = 'WELCOME HOME'
    return render_template('index.html', title = title, news = news)


@main.route('/news/<id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    final_articles = get_articles(id)
    return render_template('news.html',final_articles = final_articles )    
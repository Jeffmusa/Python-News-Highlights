from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_photos

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting photos
    photos = get_photos()
    print('photos')
    
    return render_template('index.html',photos = photos)



# Python-News-Highlights

## Built By [Jeff Musa](https://github.com/jeffmusa/)

## On 31st Aug 2018

## Description
Python-News-Highlights is a Python news application which brings you all the news sources World wide and the top headlines. Clicking on the link provided under the news source will lead the user to the articles of the source. It achieves this by using the [News API](https://newsapi.org/).

You can view the site at: [Jeff News Highlights](https://jeffmusa.herokuapp.com/).

## User Stories
These are the behaviours that the application implements to be used by a user.

As a user I would like to:
* See various news sources 
* Select the ones they prefer
* See the top-headlines of the articles from that news source
* See the image, description and time the news article was created
* Click on an article and read it fully from the news source

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed on landing page |
| Display articles from a news source | **View articles** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click an article** | Redirected to the the entire article |

## SetUp / Installation Requirements
* python3.6
* pip
* virtualenv

### Cloning
* In your terminal:
        
        $ git clone https://github.com/Jeffmusa/Python-News-Highlights.git
        $ cd Python-News-Highlights

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
         
        
* Installing Flask and other Modules

        $ python3.6 -m pip install Flask
        $ python3.6 -m pip install Flask-Bootstrap
        $ python3.6 -m pip install Flask-Script
        
* Setting up the API Key
        
        To be able to gather article info from the News API you will need an API Key.
        
        * Visit https://newsapi.org/ and register for an API key.
        * In the root directory of the project folder create a file: start.sh
        * Insert the following info into it: 
        
                export NEWS_API_KEY='<Your-Api-Key>'
                python3.6 manage.py server
                
        * Insert the API Key you received from News Api where <Your-Api-Key> is.
        
* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh
        
## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py tests
        
## Technologies Used
* Python3.6
* Flask

## License
MIT &copy;2018 [Jeff Musa](https://github.com/jeffmusa/)

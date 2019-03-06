import os

class Config:
    '''
    General config class
    '''

    ROVER_API_SOURCES_URL ='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1337&api_key={}'


    ROVER_API_KEY = os.environ.get('ROVER_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

class ProdConfig(Config):
     
    pass   

class DevConfig(Config):
    DEBUG = True     

config_options = {
'development':DevConfig,
'production':ProdConfig
}    

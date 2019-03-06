class Config:
    '''
    General config class
    '''

    ROVER_API_SOURCES_URL ='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1337&api_key={}'
                            
    pass

class ProdConfig(Config):
    '''
     Production config child class

     Args:
         The parent configuration class with General configuration settings
    '''  
    pass   

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True     

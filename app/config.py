from distutils.debug import DEBUG


class Config:
    '''General configuration for parent class'''

    NEWS_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'

class ProdConfig(Config):
    '''Production class config'''
    pass

class DevConfig(Config):
    '''Development class configuration'''
    DEBUG = True
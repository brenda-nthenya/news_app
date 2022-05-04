
import os

class Config:
    '''General configuration for parent class'''
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    CAT_API_URL = 'https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'

class ProdConfig(Config):
    '''Production class config'''
    pass

class DevConfig(Config):
    '''Development class configuration'''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production': ProdConfig
}
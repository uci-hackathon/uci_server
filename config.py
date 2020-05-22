import os


class Config(object):
    DEBUG = False
    TESTING = False
    CHAIN_API_URL = os.getenv('CHAIN_API_URL')
    ACCOUNT_KEY = os.getenv('ACCOUNT_KEY')
    ACCOUNT_NAME = os.getenv('ACCOUNT_NAME')
    FLASK_ENV = os.getenv('FLASK_ENV')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)

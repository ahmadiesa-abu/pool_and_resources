import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    USER_NAME = os.getenv('DB_USERNAME', 'pools')
    PASSWORD = os.getenv('DB_PASSWORD', 'pool1234')
    DATABASE_HOST = os.getenv('DB_HOST', 'localhost')
    DATABASE_PORT = os.getenv('DB_PORT', '5432')
    DATABASE_NAME = os.getenv('DB_NAME', 'pools')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://'+Config.USER_NAME+':'+Config.PASSWORD + \
        '@'+Config.DATABASE_HOST+':'+Config.DATABASE_PORT+'/'+Config.DATABASE_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://'+Config.USER_NAME+':'+Config.PASSWORD + \
        '@'+Config.DATABASE_HOST+':'+Config.DATABASE_PORT+'/'+Config.DATABASE_NAME
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    SQLALCHEMY_DATABASE_URI = 'postgresql://'+Config.USER_NAME+':'+Config.PASSWORD + \
        '@'+Config.DATABASE_HOST+':'+Config.DATABASE_PORT+'/'+Config.DATABASE_NAME
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY

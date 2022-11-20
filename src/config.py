from decouple import config

class Config():
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(Config):
    Debug = True

config = {
    'development' : DevelopmentConfig
}
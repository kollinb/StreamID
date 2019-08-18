import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        'GENERATED_RANDOM_KEY_HERE'
    TWITCH_API_KEY = os.environ.get('TWITCH_API_KEY') or \
        'TWITCH_API_KEY_HERE'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

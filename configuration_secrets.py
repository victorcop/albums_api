import configparser

from app.logger import log_error


class SecretConstants:
    def __init__(self):
        self.REDIS_DB = None
        self.REDIS_PORT = None
        self.REDIS_HOST = None
        self.DB_NAME = None
        self.DB_HOST = None
        self.DB_PASS = None
        self.DB_USER = None
        self.get_config()

    def get_config(self):
        try:
            config = configparser.ConfigParser()
            config.read('app.ini')

            mysql = config['mysql']
            redis = config['redis']

            self.DB_USER = mysql['db_user']
            self.DB_PASS = mysql['db_pass']
            self.DB_HOST = mysql['db_host']
            self.DB_NAME = mysql['db_name']

            self.REDIS_HOST = redis['redis_host']
            self.REDIS_PORT = redis['redis_port']
            self.REDIS_DB = redis['redis_db']
        except KeyError as e:
            log_error(e)
            
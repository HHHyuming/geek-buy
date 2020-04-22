import logging
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class LogConfig:
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0

    LOG_PATH = os.path.join(BASE_DIR, 'log')


class BaseConfig:
    DEBUG = False



class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/mogujie?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/mogujie?charset=utf8mb4'


config_map = {
    'default': DevConfig,
    'production': ProConfig,
    'development': DevConfig,
}

USE_CONFIG = config_map['default']
import os
import sys

from db.DBHelper import MysqlClient

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

# db config
db_config = {
    'geek-db': {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'root',
        'db': 'imitation-geek-buy',
        'port': 3306,
        'charset': 'utf8',
    }
}

# db list
GEEK_DB = MysqlClient(**db_config.get('geek-db'))

from pymysql import Connection
from DBUtils.PooledDB import PooledDB
import pymysql

host = '127.0.0.1'
port = 3306
password = 'root'
database = 'mogujie'
charset = 'utf8'
user = 'root'
db_name = 'book37'
conn = Connection(host=host, user=user, password=password,database=database, port=port, charset=charset)


class MysqlPool:
    config = {
        'creator': pymysql,
        'host': host,
        'port': port,
        'user': user,
        'password': password,
        'db': db_name,
        'charset': charset,
        'maxconnections': 70,  # 连接池最大连接数量
        'cursorclass': pymysql.cursors.DictCursor
    }
    pool = PooledDB(**config)

    def __enter__(self):
        self.conn = MysqlPool.pool.connection()
        self.cursor = self.conn.cursor()


        return self

    def __exit__(self, type, value, trace):
        self.cursor.close()
        self.conn.close()


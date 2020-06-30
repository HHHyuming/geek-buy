from DBUtils.PooledDB import PooledDB

class Mysql:
    arg = 123


Mysql.arg = 312
Mysql().__class__.arg = 999
print(Mysql.arg)
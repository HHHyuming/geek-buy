from script.db import MysqlPool
from script.db import conn

def import_data_from_db():
    with MysqlPool() as source_db:
        sql = 'select * from shop_data'
        source_db.cursor.execute(sql)
        source_data = source_db.cursor.fetchall()

    print(source_data)
    field_list = ['id', 'shop_name', 'category', 'img_src', 'price', 'sales_num', 'comment_num', 'score', 'services', 'stock', 'collections_num']
    back_list = ['id','goods_name','category','img_link','price','sales_num','comment_num',
                 'score','services','stock','collections_num']

    table_name = 'shop'
    sql = """insert into {0}({1}) values ({2})""".format(table_name,
                                                         '`' + "`,`".join(back_list) + '`',
                                                         str(r'%s,' * len(field_list))[:-1])
    new_data_list = []
    for data_dic in source_data:
        new_data_list.append(list(data_dic.values()))
    target_cursor = conn.cursor()
    target_cursor.executemany(sql, new_data_list)
    conn.commit()

if __name__ == '__main__':
    import_data_from_db()
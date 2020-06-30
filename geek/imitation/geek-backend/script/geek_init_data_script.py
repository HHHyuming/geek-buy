import decimal

from settings import GEEK_DB
import os
import json
import inspect
import types


class InitData:
    @staticmethod
    def rotation_chart_data():
        """
        轮播图数据
        :return:
        """
        path = r'D:\code\geek\imitation\geek-backend\script\api\homeApi.json'
        data = InitData.read_json_file(path)['data']
        chart_list = data['list'][0]
        args = []
        for item in chart_list:
            img_src = item['icon_url']
            public_name = item['public_name']
            args.append([img_src,public_name])
        sql = 'insert into rotation_chart(`img_src`, `public_name`) values (%s,%s)'

        GEEK_DB.cursor.execute(sql, args)

        # 广告
        # data['list'][1]
        sql = ''
        # home menu
        # data['list'][3]
        GEEK_DB.conn.commit()


    @staticmethod
    def category_data():
        """
        分类数据
        :return:
        """
        category_path = r'D:\code\geek\imitation\geek-backend\script\api\homeApi\categories.json'
        with open(category_path, 'r', encoding='utf8') as f:
            data = json.loads(f.read())['data']['cate']
            category_name_list = []
            for item in data:
                category_name_list.append(item['name'])

            sql = 'insert into category_t(`category_name`) values(%s)'

            GEEK_DB.cursor.executemany(sql, category_name_list)
            GEEK_DB.conn.commit()
        sql = 'select `id`, `category_name` from category_t '

        GEEK_DB.cursor.execute(sql)
        category_ids = GEEK_DB.cursor.fetchall()
        goods_path = r'D:\code\geek\imitation\geek-backend\script\api\homeApi\categoriesdetail'
        insert_goods_sql = 'insert into goods_t(`goods_img`,`goods__name`,`goods_price`,`goods_desc`,`goods_type`,' \
                           '`origin_price`,`vip_price`,`category_id`,`second_type`,`total_sales`) values(%s,%s,%s,%s,' \
                           '%s,%s,%s,%s,%s,%s)'
        path_list = os.listdir(goods_path)
        insert_data = []
        for index, goods_file in enumerate(path_list):
            current_path = os.path.join(goods_path, goods_file)
            # print(index, current_path)
            read_data = InitData.read_json_file(current_path)
            current_goods_type = category_name_list[index]
            # print(category_ids)
            category_id = list(filter(lambda x: x['category_name'] == current_goods_type, category_ids))[0]['id']

            # GEEK_DB.cursor.execute('truncate category_t')
            # return
            if read_data:
                data_item = read_data['data']['cate']
                for item in data_item:
                    second_type = item['name']
                    for product in item['products']:
                        product_name = product['product_name']
                        origin_price = product['origin_price']
                        price = product['price']
                        vip_price = decimal.Decimal(product['vip_price']) if product['vip_price'] else 0
                        spec = product['spec']
                        small_image = product['small_image']
                        total_sales = product['total_sales']
                        insert_data.append(
                            [small_image, product_name, price, spec, current_goods_type, origin_price, vip_price,
                             category_id, second_type, total_sales])

        GEEK_DB.cursor.executemany(insert_goods_sql, insert_data)
        GEEK_DB.conn.commit()

        # GEEK_DB.cursor.execute('truncate category_t')

        # @staticmethod

    @staticmethod
    def your_like_data():
        path = r'D:\code\geek\imitation\geek-backend\script\api\cart\youlike.json'
        with open(path, 'r', encoding='utf8') as f:
            res = json.loads(f.read())
            # print(res)
            # print(type(res))
            insert_goods_sql = 'insert into goods_t(`goods_img`,`goods__name`,`goods_price`,`goods_desc`,`goods_type`,' \
                               '`origin_price`,`vip_price`,`category_id`,`second_type`,`total_sales`) values(%s,%s,%s,%s,' \
                               '%s,%s,%s,%s,%s,%s)'
            current_goods_type = '猜你喜欢'
            insert_data = []
            second_type = ''
            category_id = 0
            for product in res['data']['product_list']:
                product_name = product['product_name']
                origin_price = product['origin_price']
                price = product['price']
                vip_price = decimal.Decimal(product['vip_price']) if product['vip_price'] else 0
                spec = product['spec']
                small_image = product['small_image']
                total_sales = product['total_sales']
                insert_data.append([small_image, product_name, price, spec, current_goods_type, origin_price, vip_price,
                                    category_id, second_type, total_sales])
        GEEK_DB.cursor.executemany(insert_goods_sql, insert_data)
        GEEK_DB.conn.commit()

    @staticmethod
    def mixin_data():
        pass

    @staticmethod
    def read_json_file(path):
        with open(path, 'r', encoding='utf8') as f:
            data = json.loads(f.read())
            if data:
                return data


if __name__ == '__main__':
    # obj = InitData()
    # for fun_name, fun in InitData.__dict__.items():
    #     if isinstance(fun, types.FunctionType):
    #         # print(obj.__dict__)
    #         # try:
    #         getattr(obj, fun_name)()
    #         # except Exception as e:
    #         #     print(e)
    # InitData.category_data()
    # InitData.your_like_data()
    # InitData.rotation_chart_data()
    ...
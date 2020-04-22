# -*- coding: utf-8 -*-
"""
爬取内容：
流行：
新款：
精选：
分类：everything-- 上衣，裤子，裙子，鞋, 包

Created on Thu Oct 31 2019

@author:
"""
import time
import threading
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from script.db import MysqlPool
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_option.add_argument('headless')
# webdriver.Chrome(executable_path=path,options=chrome_option)
browser = webdriver.Chrome(options=chrome_option)
browser.set_window_size(1200,800)
wait = WebDriverWait(browser, 30)
url_map = {
    '上衣': "https://list.mogu.com/book/clothing/",
    "裙子": "https://list.mogu.com/book/skirt",
    "裤子": "https://list.mogu.com/book/trousers",
    "内衣": "https://list.mogu.com/book/neiy",
    "鞋子": "https://list.mogu.com/book/shoes",
    "包": "https://list.mogu.com/book/bags",
    "男友": "https://list.mogu.com/book/boyfriend",
    "母婴": "https://list.mogu.com/book/baby",
    "家具": "https://list.mogu.com/book/home"
}


def handler_url(category, url):
    data = []
    browser.get(url)
    wait.until(EC.presence_of_element_located((By.ID, "wall_goods_box")))
    scroll = True
    page = 2
    while page > 0:
        for index in range(1, 41):
            if scroll:
                browser.execute_script('window.scrollTo(0, 500)')
                scroll = False
            try:
                xpath = '//*[@class="goods_list_mod clearfix J_mod_hidebox J_mod_show"][last()]//div[{}]'.format(index)
                element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            except Exception as e:
                try:
                    traceback.print_exc()
                    print('raise error =------')
                    xpath = '//*[@class="goods_list_mod clearfix J_mod_hidebox"][1]//div[{}]'.format(index)
                    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                except Exception as e:
                    print('error index ---',index)
                    continue
                    pass
            # 进入detail 页面,获取当前window
            # time.sleep(5)
            try:
                element.click()
                all_window = browser.window_handles
                browser.switch_to.window(all_window[-1])
            except Exception as e:
                continue

            try:
                img_ele = wait.until(EC.presence_of_element_located((By.ID, 'J_BigImg')))
                img_src = img_ele.get_attribute('src')

                title_xpath = "/html/body/div[6]/div[2]/div[1]/div[1]/div/div[1]/div/h1/span[2]"
                title_ele = wait.until(EC.presence_of_element_located((By.XPATH, title_xpath)))
                shop_name = title_ele.text

                try:
                    sales_num_xpath = "/html/body/div[6]/div[2]/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div[1]/div/dl[2]/dd[2]/span[2]/span"
                    sales_num_ele = wait.until(EC.presence_of_element_located((By.XPATH, sales_num_xpath)))
                except Exception as e:
                    traceback.print_exc()
                    sales_num_xpath = "/html/body/div[6]/div[2]/div[1]/div[1]/div/div[1]/div/div[3]/div[1]/div[2]/dl[3]/dd/div[2]"
                    sales_num_ele = wait.until(EC.presence_of_element_located((By.XPATH, sales_num_xpath)))
                sales_num = sales_num_ele.text

                comment_num_xpath = "/html/body/div[6]/div[2]/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div[1]/div/dl[2]/dd[2]/span[1]/span"
                comment_num_ele = wait.until(EC.presence_of_element_located((By.XPATH, comment_num_xpath)))
                comment_num = comment_num_ele.text

                price_xpath = '//*[@id="J_NowPrice"]'
                price_ele = wait.until(EC.presence_of_element_located((By.XPATH, price_xpath)))
                price = str(price_ele.text).split('~')[0][1:]

                collections_num_xpath = "/html/body/div[6]/div[2]/div[1]/div[1]/div/div[1]/div/div[4]/div[1]/span[2]"
                collections_num_ele = wait.until(EC.presence_of_element_located((By.XPATH, collections_num_xpath)))
                collections_num = collections_num_ele.text

                services_xpath = "/html/body/div[6]/div[2]/div[1]/div[1]/div/div[1]/div/div[5]/div[1]/ul"
                services_ele = wait.until(EC.presence_of_element_located((By.XPATH, services_xpath)))
                services = services_ele.text

                # stock_xpath = '//*[@id="J_GoodsSku"]/div[1]/div[2]/dl[2]/dd/div[2]'
                stock_select = ".J_GoodsStock"
                stock_ele = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, stock_select)))
                stock = stock_ele.text
                # 获取分数
                score_click_xpath = '//*[@id="J_ModuleTabpanel"]/div[1]/ul/li[2]'
                wait.until(EC.presence_of_element_located((By.XPATH, score_click_xpath))).click()

                score_xpath = '//*[@id="J_RatesBuyer"]/div[2]/div[1]/ul/li/span[2]/b'
                score_ele = wait.until(EC.presence_of_element_located((By.XPATH, score_xpath)))
                score = score_ele.text
            except Exception as e:
                print(index)
                pass
            else:

                in_db_data = {"category": category, 'shop_name': shop_name, 'img_src': img_src, 'sales_num': sales_num,
                              'comment_num': comment_num, "price": price, "collections_num": collections_num,
                              "services": services, "score": score, "stock": stock}
                print(in_db_data)
                data.append(in_db_data)
            browser.close()
            browser.switch_to.window(all_window[0])
            # browser.save_screenshot('./{}.png'.format(browser.current_window_handle))


        # 往下滚动1000个单位，加载数据
        print('scroll ====================================')
        browser.execute_script('window.scrollTo(0, 4500)')
        browser.save_screenshot('./scroll.png')
        page -= 1
    write_to_db(data)


def get_category_data():
    # thread_list = []
    for category, url in url_map.items():
        res = handler_url(category, url)
        # obj = threading.Thread(target=handler_url, args=(category,url))
        # obj.start()
        # thread_list.append(obj)
    #
    # for th in thread_list:
    #     th.join()
    # else:
    #     print('task done')
        # browser.quit()


def write_to_db(data_list):
    """
    :param data_list:[{},{},{}]
    :return:
    """
    table_name = 'shop_data'

    field_list = ['category', 'shop_name', 'img_src', 'sales_num', 'comment_num', 'price',
                  'collections_num', 'services', 'score', 'stock']
    new_data_list = []
    for data_dic in data_list:
        new_data_list.append(list(data_dic.values()))

    with MysqlPool() as db:
        sql = """insert into {0}({1}) values ({2})""".format(table_name,
                                                             '`' + "`,`".join(field_list) + '`',
                                                             str(r'%s,' * len(field_list))[:-1])
        print(sql)
        print(new_data_list)
        db.cursor.executemany(sql, new_data_list)
        db.conn.commit()
if __name__ == '__main__':
    s = time.time()
    get_category_data()
    e = time.time()
    print('cost time -----', e-s)
    # dic = {'category': '上衣', 'shop_name': '2件50上衣女欧洲站白色t恤女短袖洋气衣服女学生韩版百搭夏季', 'img_src': 'https://s5.mogucdn.com/mlcdn/55cf19/200109_3hg13gcj0l922eijeehb6b4h2d28a_640x960.jpg_468x468.jpg', 'sales_num': '307', 'comment_num': '76', 'price': '¥28.00', 'collections_num': '783', 'services': '72小时发货7天无理由退货延误必赔退货补运费', 'score': '4.61', 'stock': '库存4515件'}
    # print(dic.values())
# -*- coding:utf-8 -*-

"""
6 爬虫程序：给定500个企业的名称，请定向爬取天眼查，得到该企业的官方网址信息；
王嘉承   软件1801   120181080414
"""

import requests
import time
import pymysql
from lxml import etree
from urllib import parse
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def return_detail_url(company_encode):
    url = f"https://www.tianyancha.com/search?key={company_encode}"

    res = requests.get(url=url, headers=header)
    tree = etree.HTML(res.text)
    detail_url = tree.xpath('//*/div[@class="result-list sv-search-container"]/div[@class="search-item '
                            'sv-search-company"][1]/div[1]/div[3]/div[1]/a/@href')
    print(detail_url)

    return detail_url


def return_weburl(detail_url):
    # detail_url = "https://www.tianyancha.com/company/3029626017"
    res_content = requests.get(url=detail_url, headers=header)
    # print(res_content.text)
    tree2 = etree.HTML(res_content.text)
    web_ur = "".join(tree2.xpath('//*/span[contains(text(), "网址：")]/following-sibling::a[1]/text()'))
    print(web_ur)
    return web_ur


if __name__ == '__main__':
    # def work(n):
    con_engine = pymysql.connect(host='localhost', user="root", password="0414666jy", database="qichacha", port=3306,
                                 charset='utf8')

    # 使用cursor()方法获取游标
    cursor = con_engine.cursor()

    # SQL语句
    sql_ = "select * from temp_icp_web2;"
    try:
        # 执行SQL语句
        cursor.execute(sql_)
        # fetchall()获取所有记录，形成的是元组，results = cursor.fetchmany(10)获取前10条，results = cursor.fetchone()获取一条数据
        results = cursor.fetchall()
        for row in results[246:500]:  # 依次获取每一行数据(此处是取的从246开始的500条记录)
            company = row[3]  # 第4列

            # company = "中国华戎科技集团有限公司"
            company_encode = parse.quote(company)

            header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                          'application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Cookie': '',  # 此处需填上本机登录天眼查网站后的cookie
                'Host': 'www.tianyancha.com',
                'Referer': f'https://www.tianyancha.com/search?key={company_encode}',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/83.0.4103.106 Safari/537.36 '
            }

            detail_url = return_detail_url(company_encode)
            if detail_url == []:
                print("出验证码了")
                time.sleep(60)  # 60s用于输入验证码
                detail_url = return_detail_url(company_encode)
            time.sleep(2)
            detail_url = detail_url[0]
            print("----", detail_url)
            # if detail_url == "0":
            #     web_url = "无"

            # else:
            web_url = return_weburl(detail_url)
            sql = "INSERT INTO webUrl(company,web_url) VALUES ('%s','%s')" % (company, web_url)

            cursor.execute(sql)
            con_engine.commit()
            print(f"{company}----插入成功")
            time.sleep(3)
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    con_engine.close()

# if __name__ == '__main__':
#     executor = ProcessPoolExecutor(max_workers=5)
#     futures = []
#     for i in range(5):
#         future = executor.submit(work, i + 1)
#         futures.append(future)
#     executor.shutdown(True)

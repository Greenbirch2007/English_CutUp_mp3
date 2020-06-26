#! -*- coding:utf-8 -*-

import urllib.request

import datetime
import re
import time
import os
import pymysql
import requests
import wget
from lxml import etree
from requests.exceptions import RequestException
from selenium import webdriver

def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
    # driver.get(url)
    # html = driver.page_source
    # return html


def mkdir(path):

    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')








def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
    lpath = os.getcwd()

    selector = etree.HTML(html)
    mp3_url = selector.xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/a[1]/@href')
    lrc_url = selector.xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/a[2]/@href')
    title_url = selector.xpath('/html/body/div[2]/div[3]/div[1]/div[1]/h1/text()')
    # 先创建文件夹
    f_path = lpath+'/'+"Family_Album_USA"
    mkdir(f_path)

    # 下载以及以及命名 使用wget进行下载
    # mp3文件下载
    mp3_name= mp3_url[0].split("/")[-1]

    # urllib.request.urlretrieve(mp3_url[0], '{0}/{1}'.format(f_path, mp3_name))
    wget.download(mp3_url[0], out=os.path.join(f_path, mp3_name))
    # #lrc文件下载
    lrc_name= lrc_url[0].split("/")[-1]
    wget.download(lrc_url[0], out=os.path.join(f_path, lrc_name))
    # urllib.request.urlretrieve(lrc_url[0], '{0}/{1}'.format(f_path, lrc_name))







if __name__ == "__main__":
    # options = webdriver.ChromeOptions()
    # options.add_argument("--no-sandbox")
    # driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)
    Family_Album_USA_L = ["http://www.tingclass.net/down-5027-277-1.html",
                          "http://www.tingclass.net/down-5027-278-1.html",
                          "http://www.tingclass.net/down-5027-279-1.html",
                          "http://www.tingclass.net/down-5027-280-1.html",
                          "http://www.tingclass.net/down-5027-281-1.html",
                          "http://www.tingclass.net/down-5027-282-1.html",
                          "http://www.tingclass.net/down-5027-283-1.html",
                          "http://www.tingclass.net/down-5027-284-1.html",
                          "http://www.tingclass.net/down-5027-285-1.html",
                          "http://www.tingclass.net/down-5027-286-1.html",
                          "http://www.tingclass.net/down-5027-287-1.html",
                          "http://www.tingclass.net/down-5027-288-1.html",
                          "http://www.tingclass.net/down-5027-289-1.html",
                          "http://www.tingclass.net/down-5027-290-1.html",
                          "http://www.tingclass.net/down-5027-291-1.html",
                          "http://www.tingclass.net/down-5027-292-1.html",
                          "http://www.tingclass.net/down-5027-293-1.html",
                          "http://www.tingclass.net/down-5027-294-1.html",
                          "http://www.tingclass.net/down-5027-295-1.html",
                          "http://www.tingclass.net/down-5027-296-1.html",
                          "http://www.tingclass.net/down-5027-297-1.html",
                          "http://www.tingclass.net/down-5027-298-1.html",
                          "http://www.tingclass.net/down-5027-299-1.html",
                          "http://www.tingclass.net/down-5027-300-1.html",
                          "http://www.tingclass.net/down-5027-301-1.html",
                          "http://www.tingclass.net/down-5027-302-1.html",
                          "http://www.tingclass.net/down-5027-303-1.html",
                          "http://www.tingclass.net/down-5027-304-1.html",
                          "http://www.tingclass.net/down-5027-305-1.html",
                          "http://www.tingclass.net/down-5027-306-1.html",
                          "http://www.tingclass.net/down-5027-307-1.html",
                          "http://www.tingclass.net/down-5027-308-1.html",
                          "http://www.tingclass.net/down-5027-309-1.html",
                          "http://www.tingclass.net/down-5027-310-1.html",
                          "http://www.tingclass.net/down-5027-311-1.html",
                          "http://www.tingclass.net/down-5027-312-1.html",
                          "http://www.tingclass.net/down-5027-313-1.html",
                          "http://www.tingclass.net/down-5027-314-1.html",
                          "http://www.tingclass.net/down-5027-315-1.html",
                          "http://www.tingclass.net/down-5027-316-1.html",
                          "http://www.tingclass.net/down-5027-317-1.html",
                          "http://www.tingclass.net/down-5027-318-1.html",
                          "http://www.tingclass.net/down-5027-319-1.html",
                          "http://www.tingclass.net/down-5027-320-1.html",
                          "http://www.tingclass.net/down-5027-321-1.html",
                          "http://www.tingclass.net/down-5027-322-1.html",
                          "http://www.tingclass.net/down-5027-323-1.html",
                          "http://www.tingclass.net/down-5027-324-1.html",
                          "http://www.tingclass.net/down-5027-325-1.html",
                          "http://www.tingclass.net/down-5027-326-1.html",
                          "http://www.tingclass.net/down-5027-327-1.html",
                          "http://www.tingclass.net/down-5027-328-1.html",
                          "http://www.tingclass.net/down-5027-329-1.html",
                          "http://www.tingclass.net/down-5027-330-1.html",
                          "http://www.tingclass.net/down-5027-331-1.html",
                          "http://www.tingclass.net/down-5027-332-1.html",
                          "http://www.tingclass.net/down-5027-333-1.html",
                          "http://www.tingclass.net/down-5027-334-1.html",
                          "http://www.tingclass.net/down-5027-335-1.html",
                          "http://www.tingclass.net/down-5027-336-1.html",
                          "http://www.tingclass.net/down-5027-337-1.html",
                          "http://www.tingclass.net/down-5027-338-1.html",
                          "http://www.tingclass.net/down-5027-339-1.html",
                          "http://www.tingclass.net/down-5027-340-1.html",
                          "http://www.tingclass.net/down-5027-341-1.html",
                          "http://www.tingclass.net/down-5027-342-1.html",
                          "http://www.tingclass.net/down-5027-343-1.html",
                          "http://www.tingclass.net/down-5027-344-1.html",
                          "http://www.tingclass.net/down-5027-345-1.html",
                          "http://www.tingclass.net/down-5027-346-1.html",
                          "http://www.tingclass.net/down-5027-347-1.html",
                          "http://www.tingclass.net/down-5027-348-1.html",
                          "http://www.tingclass.net/down-5027-349-1.html",
                          "http://www.tingclass.net/down-5027-350-1.html",
                          "http://www.tingclass.net/down-5027-351-1.html",
                          "http://www.tingclass.net/down-5027-352-1.html",
                          "http://www.tingclass.net/down-5027-353-1.html",
                          "http://www.tingclass.net/down-5027-354-1.html"]


    for one_it in Family_Album_USA_L:
        html = call_page(one_it)
        parse_html(html)
        print(one_it)
        time.sleep(10)










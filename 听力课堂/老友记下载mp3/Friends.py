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




def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = str(num1)
    return f_num
def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items



def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
    lpath = os.getcwd()

    selector = etree.HTML(html)
    mp3_url = selector.xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/a[1]/@href')
    f_mp3Url =remove_block(mp3_url)
    title_url = selector.xpath('/html/body/div[2]/div[3]/div[1]/div[1]/h1/text()')
    # 先创建文件夹
    f_path = lpath+'/'+"Friends"
    mkdir(f_path)

    # 下载以及以及命名 使用wget进行下载
    # mp3文件下载
    mp3_name= title_url[0]+f_mp3Url[0].split("/")[-1]

    # urllib.request.urlretrieve(mp3_url[0], '{0}/{1}'.format(f_path, mp3_name))
    wget.download(f_mp3Url[0], out=os.path.join(f_path, mp3_name))







if __name__ == "__main__":
    Friends_l =[
        "http://www.tingclass.net/down-5028-355-1.html", "http://www.tingclass.net/down-5028-356-1.html",
        "http://www.tingclass.net/down-5028-357-1.html", "http://www.tingclass.net/down-5028-358-1.html",
        "http://www.tingclass.net/down-5028-359-1.html", "http://www.tingclass.net/down-5028-360-1.html",
        "http://www.tingclass.net/down-5028-361-1.html", "http://www.tingclass.net/down-5028-362-1.html",
        "http://www.tingclass.net/down-5028-363-1.html", "http://www.tingclass.net/down-5028-364-1.html",
        "http://www.tingclass.net/down-5028-365-1.html", "http://www.tingclass.net/down-5028-366-1.html",
        "http://www.tingclass.net/down-5028-367-1.html", "http://www.tingclass.net/down-5028-368-1.html",
        "http://www.tingclass.net/down-5028-369-1.html", "http://www.tingclass.net/down-5028-370-1.html",
        "http://www.tingclass.net/down-5028-371-1.html", "http://www.tingclass.net/down-5028-372-1.html",
        "http://www.tingclass.net/down-5028-373-1.html", "http://www.tingclass.net/down-5028-374-1.html",
        "http://www.tingclass.net/down-5028-375-1.html", "http://www.tingclass.net/down-5028-376-1.html",
        "http://www.tingclass.net/down-5028-377-1.html", "http://www.tingclass.net/down-5028-378-1.html",
        "http://www.tingclass.net/down-5029-379-1.html", "http://www.tingclass.net/down-5029-380-1.html",
        "http://www.tingclass.net/down-5029-381-1.html", "http://www.tingclass.net/down-5029-382-1.html",
        "http://www.tingclass.net/down-5029-383-1.html", "http://www.tingclass.net/down-5029-384-1.html",
        "http://www.tingclass.net/down-5029-385-1.html", "http://www.tingclass.net/down-5029-386-1.html",
        "http://www.tingclass.net/down-5029-387-1.html", "http://www.tingclass.net/down-5029-388-1.html",
        "http://www.tingclass.net/down-5029-389-1.html", "http://www.tingclass.net/down-5029-390-1.html",
        "http://www.tingclass.net/down-5029-391-1.html", "http://www.tingclass.net/down-5029-392-1.html",
        "http://www.tingclass.net/down-5029-393-1.html", "http://www.tingclass.net/down-5029-394-1.html",
        "http://www.tingclass.net/down-5029-395-1.html", "http://www.tingclass.net/down-5029-396-1.html",
        "http://www.tingclass.net/down-5029-397-1.html", "http://www.tingclass.net/down-5029-398-1.html",
        "http://www.tingclass.net/down-5029-399-1.html", "http://www.tingclass.net/down-5029-400-1.html",
        "http://www.tingclass.net/down-5029-224255-1.html", "http://www.tingclass.net/down-5030-403-1.html",
        "http://www.tingclass.net/down-5030-404-1.html", "http://www.tingclass.net/down-5030-405-1.html",
        "http://www.tingclass.net/down-5030-406-1.html", "http://www.tingclass.net/down-5030-407-1.html",
        "http://www.tingclass.net/down-5030-408-1.html", "http://www.tingclass.net/down-5030-409-1.html",
        "http://www.tingclass.net/down-5030-410-1.html", "http://www.tingclass.net/down-5030-411-1.html",
        "http://www.tingclass.net/down-5030-412-1.html", "http://www.tingclass.net/down-5030-413-1.html",
        "http://www.tingclass.net/down-5030-414-1.html", "http://www.tingclass.net/down-5030-415-1.html",
        "http://www.tingclass.net/down-5030-416-1.html", "http://www.tingclass.net/down-5030-417-1.html",
        "http://www.tingclass.net/down-5030-418-1.html", "http://www.tingclass.net/down-5030-419-1.html",
        "http://www.tingclass.net/down-5030-420-1.html", "http://www.tingclass.net/down-5030-421-1.html",
        "http://www.tingclass.net/down-5030-422-1.html", "http://www.tingclass.net/down-5030-423-1.html",
        "http://www.tingclass.net/down-5030-424-1.html", "http://www.tingclass.net/down-5030-425-1.html",
        "http://www.tingclass.net/down-5030-426-1.html", "http://www.tingclass.net/down-5030-427-1.html",
        "http://www.tingclass.net/down-5031-428-1.html", "http://www.tingclass.net/down-5031-429-1.html",
        "http://www.tingclass.net/down-5031-430-1.html", "http://www.tingclass.net/down-5031-431-1.html",
        "http://www.tingclass.net/down-5031-432-1.html", "http://www.tingclass.net/down-5031-433-1.html",
        "http://www.tingclass.net/down-5031-434-1.html", "http://www.tingclass.net/down-5031-435-1.html",
        "http://www.tingclass.net/down-5031-436-1.html", "http://www.tingclass.net/down-5031-437-1.html",
        "http://www.tingclass.net/down-5031-438-1.html", "http://www.tingclass.net/down-5031-439-1.html",
        "http://www.tingclass.net/down-5031-440-1.html", "http://www.tingclass.net/down-5031-441-1.html",
        "http://www.tingclass.net/down-5031-442-1.html", "http://www.tingclass.net/down-5031-443-1.html",
        "http://www.tingclass.net/down-5031-444-1.html", "http://www.tingclass.net/down-5031-445-1.html",
        "http://www.tingclass.net/down-5031-446-1.html", "http://www.tingclass.net/down-5031-447-1.html",
        "http://www.tingclass.net/down-5031-448-1.html", "http://www.tingclass.net/down-5031-449-1.html",
        "http://www.tingclass.net/down-5031-450-1.html", "http://www.tingclass.net/down-5032-451-1.html",
        "http://www.tingclass.net/down-5032-452-1.html", "http://www.tingclass.net/down-5032-453-1.html",
        "http://www.tingclass.net/down-5032-454-1.html", "http://www.tingclass.net/down-5032-455-1.html",
        "http://www.tingclass.net/down-5032-456-1.html", "http://www.tingclass.net/down-5032-457-1.html",
        "http://www.tingclass.net/down-5032-458-1.html", "http://www.tingclass.net/down-5032-459-1.html",
        "http://www.tingclass.net/down-5032-460-1.html", "http://www.tingclass.net/down-5032-461-1.html",
        "http://www.tingclass.net/down-5032-462-1.html", "http://www.tingclass.net/down-5032-463-1.html",
        "http://www.tingclass.net/down-5032-464-1.html", "http://www.tingclass.net/down-5032-465-1.html",
        "http://www.tingclass.net/down-5032-466-1.html", "http://www.tingclass.net/down-5032-467-1.html",
        "http://www.tingclass.net/down-5032-468-1.html", "http://www.tingclass.net/down-5032-469-1.html",
        "http://www.tingclass.net/down-5032-470-1.html", "http://www.tingclass.net/down-5032-471-1.html",
        "http://www.tingclass.net/down-5032-472-1.html", "http://www.tingclass.net/down-5032-473-1.html",
        "http://www.tingclass.net/down-5033-474-1.html", "http://www.tingclass.net/down-5033-475-1.html",
        "http://www.tingclass.net/down-5033-476-1.html", "http://www.tingclass.net/down-5033-477-1.html",
        "http://www.tingclass.net/down-5033-478-1.html", "http://www.tingclass.net/down-5033-479-1.html",
        "http://www.tingclass.net/down-5033-480-1.html", "http://www.tingclass.net/down-5033-481-1.html",
        "http://www.tingclass.net/down-5033-482-1.html", "http://www.tingclass.net/down-5033-483-1.html",
        "http://www.tingclass.net/down-5033-484-1.html", "http://www.tingclass.net/down-5033-485-1.html",
        "http://www.tingclass.net/down-5033-486-1.html", "http://www.tingclass.net/down-5033-487-1.html",
        "http://www.tingclass.net/down-5033-488-1.html", "http://www.tingclass.net/down-5033-489-1.html",
        "http://www.tingclass.net/down-5033-490-1.html", "http://www.tingclass.net/down-5033-491-1.html",
        "http://www.tingclass.net/down-5033-492-1.html", "http://www.tingclass.net/down-5033-493-1.html",
        "http://www.tingclass.net/down-5033-494-1.html", "http://www.tingclass.net/down-5033-495-1.html",
        "http://www.tingclass.net/down-5033-496-1.html", "http://www.tingclass.net/down-5033-497-1.html",
        "http://www.tingclass.net/down-5033-498-1.html", "http://www.tingclass.net/down-5034-499-1.html",
        "http://www.tingclass.net/down-5034-500-1.html", "http://www.tingclass.net/down-5034-501-1.html",
        "http://www.tingclass.net/down-5034-502-1.html", "http://www.tingclass.net/down-5034-503-1.html",
        "http://www.tingclass.net/down-5034-504-1.html", "http://www.tingclass.net/down-5034-505-1.html",
        "http://www.tingclass.net/down-5034-506-1.html", "http://www.tingclass.net/down-5034-507-1.html",
        "http://www.tingclass.net/down-5034-508-1.html", "http://www.tingclass.net/down-5034-509-1.html",
        "http://www.tingclass.net/down-5034-510-1.html", "http://www.tingclass.net/down-5034-511-1.html",
        "http://www.tingclass.net/down-5034-512-1.html", "http://www.tingclass.net/down-5034-513-1.html",
        "http://www.tingclass.net/down-5034-514-1.html", "http://www.tingclass.net/down-5034-515-1.html",
        "http://www.tingclass.net/down-5034-516-1.html", "http://www.tingclass.net/down-5034-517-1.html",
        "http://www.tingclass.net/down-5034-518-1.html", "http://www.tingclass.net/down-5034-519-1.html",
        "http://www.tingclass.net/down-5034-520-1.html", "http://www.tingclass.net/down-5034-521-1.html",
        "http://www.tingclass.net/down-5035-522-1.html", "http://www.tingclass.net/down-5035-523-1.html",
        "http://www.tingclass.net/down-5035-524-1.html", "http://www.tingclass.net/down-5035-525-1.html",
        "http://www.tingclass.net/down-5035-526-1.html", "http://www.tingclass.net/down-5035-527-1.html",
        "http://www.tingclass.net/down-5035-528-1.html", "http://www.tingclass.net/down-5035-529-1.html",
        "http://www.tingclass.net/down-5035-530-1.html", "http://www.tingclass.net/down-5035-531-1.html",
        "http://www.tingclass.net/down-5035-532-1.html", "http://www.tingclass.net/down-5035-533-1.html",
        "http://www.tingclass.net/down-5035-534-1.html", "http://www.tingclass.net/down-5035-535-1.html",
        "http://www.tingclass.net/down-5035-536-1.html", "http://www.tingclass.net/down-5035-537-1.html",
        "http://www.tingclass.net/down-5035-538-1.html", "http://www.tingclass.net/down-5035-539-1.html",
        "http://www.tingclass.net/down-5035-540-1.html", "http://www.tingclass.net/down-5035-541-1.html",
        "http://www.tingclass.net/down-5035-542-1.html", "http://www.tingclass.net/down-5035-543-1.html",
        "http://www.tingclass.net/down-5035-544-1.html", "http://www.tingclass.net/down-5036-545-1.html",
        "http://www.tingclass.net/down-5036-546-1.html", "http://www.tingclass.net/down-5036-547-1.html",
        "http://www.tingclass.net/down-5036-548-1.html", "http://www.tingclass.net/down-5036-549-1.html",
        "http://www.tingclass.net/down-5036-550-1.html", "http://www.tingclass.net/down-5036-551-1.html",
        "http://www.tingclass.net/down-5036-552-1.html", "http://www.tingclass.net/down-5036-553-1.html",
        "http://www.tingclass.net/down-5036-554-1.html", "http://www.tingclass.net/down-5036-555-1.html",
        "http://www.tingclass.net/down-5036-556-1.html", "http://www.tingclass.net/down-5036-557-1.html",
        "http://www.tingclass.net/down-5036-558-1.html", "http://www.tingclass.net/down-5036-559-1.html",
        "http://www.tingclass.net/down-5036-560-1.html", "http://www.tingclass.net/down-5036-561-1.html",
        "http://www.tingclass.net/down-5036-562-1.html", "http://www.tingclass.net/down-5036-563-1.html",
        "http://www.tingclass.net/down-5036-564-1.html", "http://www.tingclass.net/down-5036-565-1.html",
        "http://www.tingclass.net/down-5036-566-1.html", "http://www.tingclass.net/down-5036-567-1.html",
        "http://www.tingclass.net/down-5036-568-1.html", "http://www.tingclass.net/down-5037-569-1.html",
        "http://www.tingclass.net/down-5037-570-1.html", "http://www.tingclass.net/down-5037-571-1.html",
        "http://www.tingclass.net/down-5037-572-1.html", "http://www.tingclass.net/down-5037-573-1.html",
        "http://www.tingclass.net/down-5037-574-1.html", "http://www.tingclass.net/down-5037-575-1.html",
        "http://www.tingclass.net/down-5037-576-1.html", "http://www.tingclass.net/down-5037-577-1.html",
        "http://www.tingclass.net/down-5037-578-1.html", "http://www.tingclass.net/down-5037-579-1.html",
        "http://www.tingclass.net/down-5037-580-1.html", "http://www.tingclass.net/down-5037-581-1.html",
        "http://www.tingclass.net/down-5037-582-1.html", "http://www.tingclass.net/down-5037-583-1.html",
        "http://www.tingclass.net/down-5037-584-1.html", "http://www.tingclass.net/down-5037-585-1.html"
    ]



    for one_it in Friends_l:
        try:

            html = call_page(one_it)
            parse_html(html)
            print(one_it)

        except:
            pass


# 20 23 26 * *  /usr/bin/python3 /root/f.py








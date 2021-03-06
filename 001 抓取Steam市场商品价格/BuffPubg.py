#!/usr/bin/env python3
#encoding = utf-8


from selenium import webdriver
import time
import csv


def buff_pubg():
    pubg_price = {}
    for page in range(1,13):
        url = ('https://buff.163.com/market/?game=pubg#tab=selling&page_num=%s&sort_by=price.desc' %page)
        print('第%s页:'%page,url)
        pubg_headers = ['name','money']
        driver = webdriver.Firefox()
        driver.get(url)

        for i in range(1,21):
            #获取饰品名称和价格
            try:
                name = driver.find_element_by_xpath(
                    ('/html/body/div[6]/div/div[4]/div[1]/ul/li[%s]/h3/a') %i)
                money = driver.find_element_by_xpath(
                    ('/html/body/div[6]/div/div[4]/div[1]/ul/li[%s]/p/strong') %i)
                pubg_price[name.text] = money.text[1:] #把饰品名称和对应的价格写入到字典里面
            except:
                pass

        driver.close()
    #print(len(buff))
    #写入内容到csv文件
    try:
        with open('buff_pubg.csv', 'a+', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=pubg_headers)
            writer.writeheader()
            for k,v in pubg_price.items():
                #print(k,v)
                writer.writerow({'name': k, 'money': v})
            csvfile.close()
    except:
        pass


def buff_dota2():
    dota2_price = {}
    for page in range(1,327): #327
        url = ('https://buff.163.com/market/?game=dota2#tab=selling&page_num=%s&sort_by=price.desc' %page)
        print('第%s页'%page, url)
        dota2_headers = ['name','money']
        dota2_driver = webdriver.Firefox()
        dota2_driver.get(url)

        for i in range(1,21):
            #获取Dota2饰品价格
            try:
                dota2_name = dota2_driver.find_element_by_xpath(
                    ('/html/body/div[6]/div/div[4]/div[1]/ul/li[%s]/h3/a') %i)
                dota2_money = dota2_driver.find_element_by_xpath(
                    ('/html/body/div[6]/div/div[4]/div[1]/ul/li[%s]/p/strong') %i)
                dota2_price[dota2_name.text] = dota2_money.text[1:]
                #print(dota2_price)
            except:
                pass

        dota2_driver.close()
    #print(dota2_price)
    #把内容写入csv文件
    try:
        with open('buff_dota2.csv', 'a+', newline='') as csvdota2:
            writer = csv.DictWriter(csvdota2,fieldnames=dota2_headers)
            writer.writeheader()
            for k,v in dota2_price.items():
                #print(k,v)
                writer.writerow({'name':k, 'money':v})
            csvdota2.close()
    except:
        pass

if __name__ == '__main__':
    #buff_pubg()
    buff_dota2()

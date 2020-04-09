
import requests
import pymysql
import time
from lxml import etree
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
html = requests.get('https://www.ituring.com.cn/tag/2998',headers=header).text
res = etree.HTML(html)
#因为要获取标题文本，所以xpath表达式要追加/text(),res.xpath返回的是一个列表，且列表中只有一个元素所以追加一个[0]
a = res.xpath('//*[@id="tag-article"]/div[2]/ul/li')
print(len(a))
db = pymysql.connect("localhost","root","123456","graduationproject")
cursor = db.cursor()
i = 1
while i <= len(a):
    title = res.xpath(f'//*[@id="tag-article"]/div[2]/ul/li[{i}]/h2/a/text()')
    path = res.xpath(f'//*[@id="tag-article"]/div[2]/ul/li[{i}]/h2/a/@href')
    link = 'https://www.ituring.com.cn' + path[0]
    date = time.strftime('%Y:%m:%d %H:%M:%S',time.localtime(time.time()))
    sql = f"""INSERT INTO artical(title,link,date) VALUES (\'{title[0]}\',\'{link}\',\'{date}\' )"""
    result = cursor.execute(sql)
    print(result)
    db.commit()
    i+=1

html2 = requests.get('http://www.eepw.com.cn/tech/s/k/%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%86',headers=header).text
res2 = etree.HTML(html2)
#因为要获取标题文本，所以xpath表达式要追加/text(),res.xpath返回的是一个列表，且列表中只有一个元素所以追加一个[0]
a2 = res2.xpath('//*[@id="tecmain"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li')
print(len(a2))
i2 = 1
while i2 <= len(a2):
    title = res2.xpath(f'//*[@id="tecmain"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li[{i2}]/div[2]/div[1]/a/text()')
    if title == []:
        title = res2.xpath(f'//*[@id="tecmain"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li[{i2}]/div[1]/div[1]/a/text()')
    # print(title)
    path = res2.xpath(f'//*[@id="tecmain"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li[{i2}]/div[1]/a/@href')
    if path == []:
        path = res2.xpath(f'//*[@id="tecmain"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li[{i2}]/div[1]/div[1]/a/@href')
    # link =  path[0]
    # print(path)
    date = res2.xpath(f'//*[@id="tecmain"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li[{i2}]/div[2]/div[2]/span[2]/text()')
    if date == []:
        date = res2.xpath(f'//*[@id="tecmain"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li[{i2}]/div[1]/div[2]/span[2]/text()')
    # print(date)
    # date = time.strftime('%Y:%m:%d %H:%M:%S',time.localtime(time.time()))
    sql = f"""INSERT INTO artical(title,link,date) VALUES (\'{title[0]}\',\'{path[0]}\',\'{date[0]}\' )"""
    result = cursor.execute(sql)
    # print(result)
    db.commit()
    i2+=1

html3 = requests.get('https://bbs.csdn.net/forums/VC_ImageProcessing',headers=header).text
res3 = etree.HTML(html3)
# print(html3)
#因为要获取标题文本，所以xpath表达式要追加/text(),res.xpath返回的是一个列表，且列表中只有一个元素所以追加一个[0]
a3 = res3.xpath('/html/body/div[3]/div[2]/div[2]/div[3]/table/tbody/tr')
print(len(a3))
i3 = 1
while i3 <= len(a3):
    title = res3.xpath(f'/html/body/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[{i3}]/td[3]/a[2]/text()')
    # if title == []:
    #     title = res3.xpath(f'//*[@id="tecmain"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li[{i2}]/div[1]/div[1]/a/text()')
    print(title)
    path = res3.xpath(f'/html/body/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[{i3}]/td[3]/a[2]/@href')
    # if path == []:
    #     path = res3.xpath(f'//*[@id="tecmain"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li[{i2}]/div[1]/div[1]/a/@href')
    # link =  path[0]
    print(path)
    date = res3.xpath(f'/html/body/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[{i3}]/td[6]/em/text()')
    # if date == []:
    #     date = res3.xpath(f'//*[@id="tecmain"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li[{i2}]/div[1]/div[2]/span[2]/text()')
    print(date)
    # date = time.strftime('%Y:%m:%d %H:%M:%S',time.localtime(time.time()))
    sql = f"""INSERT INTO artical(title,link,date) VALUES (\'{title[0]}\',\'{path[0]}\',\'{date[0]}\' )"""
    result = cursor.execute(sql)
    # print(result)
    db.commit()
    i3+=1

db.close()
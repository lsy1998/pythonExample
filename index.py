# import urllib.request
# from bs4 import BeautifulSoup
# import pymysql
# import io
# import sys
# # import Requests
# from urllib.request import urlopen, Request
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
# url = 'https://movie.douban.com/top250'
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# movielist=[]


# def get_html(url,header):
#     ret = Request(url, headers=header)
#     res = urlopen(ret)
#     aa = res.read().decode('utf-8')
#     return aa


# def parse_html(htmlfile):
#     mysoup = BeautifulSoup(htmlfile, 'html.parser')
#     movie_zone = mysoup.find('ol')
#     movie_list = movie_zone.find_all('li')
#     for movie in movie_list:
#         movie_name = movie.find('span', attr={'class', 'title'}).getText()
#         movielist.append(movie_name)



# def save_data():

# result = get_html(url,header)

# print(result)

"""
爬取豆瓣电影Top250
"""

# import sys
# import os
# import re
# import time
# import requests
# from bs4 import BeautifulSoup


# def download(url, page):
#     print(f"正在爬取：{url}")
#     html = requests.get(url).text   # 这里不加text返回<Response [200]>
#     soup = BeautifulSoup(html, 'html.parser')
#     lis = soup.select("ol li")
#     for li in lis:
#         index = li.find('em').text
#         title = li.find('span', class_='title').text
#         rating = li.find('span', class_='rating_num').text
#         strInfo = re.search("(?<=<br/>).*?(?=<)", str(li.select_one(".bd p")), re.S | re.M).group().strip()
#         infos = strInfo.split('/')
#         year = infos[0].strip()
#         area = infos[1].strip()
#         t = infos[2].strip()
#         print(index, title, rating, year, area, t)
#         # write_fo_file(index, title, rating, year, area, type)
#     # page += 25
#     # if page < 250:
#     #     time.sleep(2)
#     #     download(f"https://movie.douban.com/top250?start={page}&filter=", page)


# # def write_fo_file(index, title, rating, year, area, type):
# #     f = open('D:/movie_top250.csv', 'a')
# #     f.write(f'{index},{title},{rating},{year},{area},{type}\n')
# #     f.closed


# def main():
#     print(os.path)
#     if os.path.exists('movie_top250.csv'):
#         os.remove('movie_top250.csv')

#     url = 'https://movie.douban.com/top250'
#     download(url, 0)
#     print("爬取完毕。")


# if __name__ == '__main__':
#     main()
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
# score = res.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[2]/span[2]/text()')[0].strip()
# comment = res.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[2]/span[3]/text()')[0].strip()
# info = res.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/p[1]/text()')[0].strip()

# print(link)
# print(date)
# 打开数据库连接
db = pymysql.connect("localhost","root","123456","graduationproject")
print(db)
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
i = 1
while i <= len(a):
    # print(i)
    title = res.xpath(f'//*[@id="tag-article"]/div[2]/ul/li[{i}]/h2/a/text()')
    # print(title)
    path = res.xpath(f'//*[@id="tag-article"]/div[2]/ul/li[{i}]/h2/a/@href')
    # print(path)
    link = 'https://www.ituring.com.cn' + path[0]
    # print(link)
    date = time.strftime('%Y:%m:%d %H:%M:%S',time.localtime(time.time()))
# # SQL 插入语句
    sql = f"""INSERT INTO artical(title,link,date) VALUES (\'{title[0]}\',\'{link}\',\'{date}\' )"""
    # print(sql)
#    # 执行sql语句
    result = cursor.execute(sql)
    print(result)
#    # 提交到数据库执行
    db.commit()
    i+=1
# 关闭数据库连接
db.close()
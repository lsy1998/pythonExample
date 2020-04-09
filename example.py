import requests
import pymysql
from bs4 import BeautifulSoup
url="https://bbs.csdn.net/forums/VC_ImageProcessing"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
ss=None
db = pymysql.connect("localhost","root","123456","graduationproject")
cursor = db.cursor()
try:
    r=requests.get(url,headers=headers,timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    # 下面的这种方法会报错   TypeError("'NoneType' object is not callable")
    # ss=soup.findall("class",class_="article-item-box csdn-tracking-statistics")
    # 找到所有class为article-item-box csdn-tracking-statistics的节点
    # for sss in soup.findAll(name="tr", attrs={"class": "forums_title"}):
    for s in soup.findAll(name="tr"):

        ss = s.findAll(name="td", attrs={"class": "forums_topic"})
        Title = 'lsy' 
        Link = 'lsy'
        Date = 'lsy'
        if ss != []:
            title = ss[0].findAll(name="a", attrs={"class": "forums_title"})
            if title != []:
                Title = title[0].getText()
                Link = 'https://bbs.csdn.net'+title[0]['href']
                
                
        sss = s.findAll(name="td", attrs={"class": "forums_last_pub"})
        if sss != []:
            date = sss[0].findAll(name="em")
            if date != []:
                Date = date[0].getText()
        # print(TITLE)
        # print(LINK)
        # print(Title)
        # print(Link)
        # print(Date)
        if Title != 'lsy':
            print(Link)
            sql = f"""INSERT INTO artical(title,link,date) VALUES (\'{Title}\',\'{Link}\',\'{Date}\' )"""
            print(sql)
            result = cursor.execute(sql)
            db.commit()

except Exception as e:
    print("出现异常------异常信息："+repr(e))

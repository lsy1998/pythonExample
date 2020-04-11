import os
import pymysql
db = pymysql.connect("localhost","root","123456","graduationproject")
cursor = db.cursor()
path = r'C:\Users\hasee\Desktop\dicomPic'
fileList = os.listdir(path)
print(fileList)

for j in range(len(fileList)-1):
    for k in range(len(fileList)-1):
        if int(fileList[k]) > int(fileList[k+1]):
            t = int(fileList[k])
            fileList[k] = int(fileList[k+1])
            fileList[k+1] = t
print(fileList)

for name in fileList:
    sql = f"""INSERT INTO dicompic(dicomPath) VALUES (\'{name}\')"""
    print(sql)
    result = cursor.execute(sql)
    db.commit()

for name in fileList:
    childPath = r'C:\Users\hasee\Desktop\dicomPic'
    childPath = childPath + '\\'
    childPath = childPath + str(name)
    childFileList = os.listdir(childPath)
    print(len(childFileList)-1)
    print(childFileList)
    childPath = ''
    sql = f"""update dicompic set dicomLength = {len(childFileList)-1} where dicomPath = \'{str(name)}\'"""
    print(sql)
    result = cursor.execute(sql)
    db.commit()


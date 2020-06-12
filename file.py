import os
import pymysql
db = pymysql.connect("localhost","root","123456","graduationproject")
cursor = db.cursor()
path = r'C:\Users\hasee\Desktop\dicom'
fileList = os.listdir(path)
print(fileList)

# for j in range(len(fileList)-1):
#     for k in range(len(fileList)-1):
#         if int(fileList[k]) > int(fileList[k+1]):
#             t = int(fileList[k])
#             fileList[k] = int(fileList[k+1])
#             fileList[k+1] = t
# print(fileList)

for name in fileList:
    # sql = f"""INSERT INTO dicomfile(name) VALUES (\'{name}\')"""
    # print(sql)
    # cursor.execute(sql)
    # db.commit()
    path = f'E:\LIDC-IDRI\{name}'
    fileList1 = os.listdir(path)
    for path in fileList1:
        # sql1 = f"INSERT INTO dicomfile(path) VALUES (\'{path}\') where name = \'{name}\'"
        # cursor.execute(sql1)
        # db.commit()
        path1 = f'E:\LIDC-IDRI\{name}\{path}'
        fileList2 = os.listdir(path1)
        for path2 in fileList2:
            # sql2 = f"INSERT INTO dicomfile(path1) VALUES (\'{path2}\') where name = \'{name}\' and path = \'{path2}\'"
            # cursor.execute(sql2)
            # db.commit()
            path3 = f'E:\LIDC-IDRI\{name}\{path}\{path2}'
            fileList3 = os.listdir(path3)
            for path4 in fileList3:
                # str = path2 + '\\'
                # str1 = str +path4
                # print(str1)
                sql3 = f"INSERT INTO dicomfile(name,path,path1,path2,path3,length1,length2) VALUES (\'{name}\',\'{path}\',\'{path2}\',\'{path4}\',\'wadouri:http://localhost:8082/dicomPic/{name}/{path}/{path2}/{path4}\',{len(fileList1)},{len(fileList3)}) "
                cursor.execute(sql3)
                db.commit()



# for name in fileList:
#     childPath = r'C:\Users\hasee\Desktop\dicomPic'
#     childPath = childPath + '\\'
#     childPath = childPath + str(name)
#     childFileList = os.listdir(childPath)
#     print(len(childFileList)-1)
#     print(childFileList)
#     childPath = ''
#     sql = f"""update dicompic set dicomLength = {len(childFileList)-1} where dicomPath = \'{str(name)}\'"""
#     print(sql)
#     result = cursor.execute(sql)
#     db.commit()


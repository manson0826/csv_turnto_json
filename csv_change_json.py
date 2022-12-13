# -*- coding: utf-8 -*-
import csv    # Python standard library中的csv模組。
import os
import json
data = []

# 讀取csv檔內容，放到csvDataToRead變數中。
csvFileToRead = open('D:/flask_server/cncdata/test.csv', 'r', encoding='utf-8-sig')
csvDataToRead = csv.reader(csvFileToRead)

# 將csvDataToRead(原csv檔內容)轉為list。
dataList = list(csvDataToRead)
# 注意：必須在轉完list之後才關檔，否則會產生'ValueError: I/O operation on closed file.'
# 　　　的exception。
for row in dataList:
    data.append(row)
    print("DOING!!!")
json_data = json.dumps(data)
csvFileToRead.close()
print(dataList)



# 修改list內容。
print(dataList)

with open(r'D:/flask_server/cncdata/test.json', 'w') as jsonFile: #原本的資料會被蓋過去
	jsonFile.write(json_data)
	jsonFile.close()
print("DONE!!")

import json
import csv

with open('csvファイルのパス','r') as c:
    reader = csv.reader(c)
    for index,row in enumerate(reader):
        #書き込みたいjsonの内容
        data = {
            'No': row[0],
            'Name': row[1],
            'Job': row[2]
        }
        with open('作成したいjsonファイルのパス/test{}.json'.format(index+1), 'w') as f:
            #json形式にエンコード
            json.dump(data,f,indent=4)

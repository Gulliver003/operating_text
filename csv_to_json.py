#-*- coding: utf-8 -*-
import json
import csv
from collections import OrderedDict

with open('/Users/sugiuratakuya/st.csv','r') as c:
    reader = csv.reader(c)
    for index,row in enumerate(reader):
        #書き込みたいjsonの内容
        od = OrderedDict([
            ('No',row[0]),
            ('Name',row[1]),
            ('Job','Manager'),
            ('A', OrderedDict([('i', row[2]), ('j', 2)])),
            ('B', OrderedDict([('k', 1), ('l', 2)])),
            ('Text', 'Hello world'),
        ])
        '''
        以下のように書き込まれる
        {
            "No": "1",
            "Name": "takuya",
            "Job": "Manager",
            "A": {
                "i": "programmer",
                "j": 2
            },
            "B": {
                "k": 1,
                "l": 2
            },
            "Text": "Hello world"
        }
        '''
        with open('/Users/sugiuratakuya/testjson/test{}.json'.format(index+1), 'w') as f:
            #json形式にエンコード
            json.dump(od,f,indent=4)

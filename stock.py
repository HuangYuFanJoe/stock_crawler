import requests
import pandas as pd
import numpy as np
from io import StringIO

date = '20210310'
r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + date + '&type=ALL')

# 篩選出個股盤後資訊
str_list = []
for i in r.text.split('\n'):
    if len(i.split('",')) == 17 and i[0] != '=':       
        i = i.strip(",\r\n")
        str_list.append(i)      

# 印出選股資訊
df = pd.read_csv(StringIO("\n".join(str_list)))  
pd.set_option('display.max_rows', None)
df.head(150)


### #股票代號
index = list(df['證券代號']).index('9943')
df.loc[index:index]

# 股票名稱
index = list(df['證券名稱']).index('台積電')
df.loc[index:index]

# 挑選本益比小於10的股票
df[(pd.to_numeric(df['本益比'], errors='coerce') < 10) &
  (pd.to_numeric(df['本益比'], errors='coerce') > 0)] ###

# 存成csv檔
df.to_csv('stock\Result.csv', encoding='utf_8_sig')
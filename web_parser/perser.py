import pandas as pd
import requests
from bs4 import (BeautifulSoup)

URL = 'https://anylink/index.html'
req = requests.get(URL)
soup = BeautifulSoup(req.text, 'lxml')
name_df = []
for row in soup.find_all(
    'tr'
):
    name_df.append(row.text)

name_df.pop(0)
size = len(name_df)
res = []
for i in range(size):
    z = name_df[i]
    z = z.split('\n')
    for j in z:
        if j == '':
            z.remove(j)
    res.append(z)
column1 = []
column2 = []
column_n = []
for i in range(len(res)):
    column1.append(res[i][0])
    column2.append(res[i][1])
    column_n.append(res[i][n])   
col = ['Название 1', 'Название 2', 'Название n']
df = pd.DataFrame(columns=col)
df['Название 1'] = column1
df['Название 2'] = column2
df['Название n'] = column_n
print(df)

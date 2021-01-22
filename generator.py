import requests
import json
import sqlite3 as sl

url ='http://www.recipepuppy.com/api/.'
querystring = {'url':'http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3'}
response = requests.request('GET', url, params=querystring)
#print(response.text)

json_obj=json.loads(response.text)

data_list= []
n=1
for results in (json_obj ['results']):
    rec= (n, results['title'], results ['ingredients'])
    n= n+1
    data_list.append(rec)

con= sl.connect('recipe.db')

try:
    with con:
        con.execute("""          
            CREATE TABLE RECIPES (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                ingredients TEXT
                 );
        """)
except:
    print ('This table already exists')

with con:
    data= con.execute ("DELETE FROM RECIPES")

sql = 'INSERT INTO RECIPES (id, title, ingredients) values(?, ?, ?)'
with con:
    con.executemany(sql, data_list)

with con:
    data= con.execute ('SELECT * FROM RECIPES')
    for row in data:
        print(row)

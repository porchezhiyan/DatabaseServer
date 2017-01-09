import web
import xml.etree.ElementTree as ET
import MySQLdb
import json
import collections



urls = (
    '/provider/', 'list_provider',
    '/subscriber/', 'list_subscriber'
)

app = web.application(urls, globals())

datap={}
datas={}



db = MySQLdb.connect(host = "127.0.0.1",
                     user = "root" ,
                     passwd = "110707",
                     db = "db1")
cur = db.cursor()
db.begin()




class list_provider:        
    def GET(self):
        cur.execute("""SELECT service, name, age FROM providers""")
        rows = cur.fetchall()
        objects_list = []       
        for row in rows:
            d = collections.OrderedDict()
            d['service'] = row[0]
            d['name'] = row[1]
            d['age'] = row[2]
            objects_list.append(d)

        j1 = json.dumps(objects_list)
        return j1

class list_subscriber:        
    def GET(self):
        cur.execute("""SELECT service, name, age FROM providers""")
        rows = cur.fetchall()
        objects_list = []       
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0]
            d['name'] = row[1]
            d['age'] = row[2]
            objects_list.append(d)

        j2 = json.dumps(objects_list)
        return j2
if __name__ == "__main__":
    app.run()

import web
import xml.etree.ElementTree as ET
import json

tree = ET.parse('sys_data.xml')
root = tree.getroot()

urls = (
    '/provider/', 'list_provider',
    '/subscriber/', 'list_subscriber'
)

app = web.application(urls, globals())

datap={}
datas={}

class list_provider:        
    def GET(self):
        i=1
        data2={}
        for child in root:
            if child.tag == "provider":
                print ('child', child.tag, child.attrib)
                data2.update({i:child.attrib})
                i+=1
        datap["providers"]=data2
        json_data1=json.dumps(datap)
        return json_data1

class list_subscriber:
    def GET(self):
        i=1
        data2={}
        for child in root:
            if child.tag == "subscriber":
                print ('child', child.tag, child.attrib)
                data2.update({i:child.attrib})
                i+=1
        datas["subscribers"]=data2
        json_data2=json.dumps(datas)
        return json_data2
if __name__ == "__main__":
    app.run()

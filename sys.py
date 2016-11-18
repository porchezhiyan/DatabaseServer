import web
import xml.etree.ElementTree as ET

tree = ET.parse('sys_data.xml')
root = tree.getroot()
root1 = tree.getroot()

urls = (
    '/provider/', 'list_provider',
    '/subscriber/', 'list_subscriber'
)

app = web.application(urls, globals())

class list_provider:        
    def GET(self):
        output = 'providers:['
        for child in root:
            if child.tag == "provider":
                print ('child', child.tag, child.attrib)
                output += str(child.attrib) + ','
        output += ']'
        return output

class list_subscriber:
    def GET(self):
        output = 'subscribers:['
        for child1 in root1:
            if child1.tag == "subscriber":
                print ('child', child1.tag, child1.attrib)
                output += str(child1.attrib) + ','
        output += ']'
        return output
if __name__ == "__main__":
    app.run()

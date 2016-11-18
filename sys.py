import web
import xml.etree.ElementTree as ET

tree = ET.parse('sys_data.xml')
root = tree.getroot()

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
        for child in root:
            if child.tag == "subscriber":
                print ('child', child.tag, child.attrib)
                output += str(child.attrib) + ','
        output += ']'
        return output
if __name__ == "__main__":
    app.run()

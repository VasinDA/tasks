import re

class HtmlParser:
    def getTextFromFile(self, filename):
        list = self.readFromFile(filename)
        for i in list:
            return re.sub(r'<[^>]+>', '', i.strip('\n'))
         
    def readFromFile(self, filename):
        try:
            with open(filename, 'r') as file:
                import_list = file.readlines()
            return import_list
        except(IOError):
            raise IOError("Reading file error")
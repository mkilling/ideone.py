from SOAPpy import WSDL


def createTuple(item):
    return (item['key'], item['value']) 

def createDict(items):
    dict = {}
    for item in items:
        key = item['key'] 
        value = item['value']
        dict[key] = value
    return dict

class IdeOne:
    def __init__(self, user='test', password='test'):
        self._user = user
        self._password = password
        self._wsdlObject = WSDL.Proxy('http://ideone.com/api/1/service.wsdl')

    def testFunction(self):
        """call ideone test function"""
        response = self._wsdlObject.testFunction('test', 'test')
        items = response['item']
        return createDict(items)

    def getLanguages(self):
        """returns a list of tuples with languages supported by ideone"""
        response = self._wsdlObject.getLanguages(self._user, self._password)
        languages = response['item'][1]['value']['item']
        return createDict(languages)

    def createSubmission(self, code, language, input='', run=True, private=False):
        response = self._wsdlObject.createSubmission(self._user, self._password, code, language, input, run, private)
        link = response['item'][1]['value']
        return link



if __name__ == "__main__":
    PYTHON = 116
    ideone = IdeOne()
    print ideone.getLanguages()
    print ideone.testFunction()
    print ideone.createSubmission("print 'Hello World'\n", PYTHON, 'lala', False, True)

from SOAPpy import WSDL

class Status:
    Waiting = -1
    Done = 0
    Compiling = 1
    Running = 3

class Result:
    NotRunning = 0
    CompileError = 11
    RuntimeError = 12
    Timeout = 13
    Success = 15
    MemoryLimit = 17
    IllegalSystemCall = 19
    InternalError = 20
    

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

    def getSubmissionStatus(self, link):
        response = self._wsdlObject.getSubmissionStatus(self._user, self._password, link)
        status = response['item'][1]['value']
        result = response['item'][2]['value']
        if status < 0: status = -1
        return (status, result)


if __name__ == "__main__":
    PYTHON = 116
    ideone = IdeOne()
    link = ideone.createSubmission("print 'Hello World'\n", PYTHON)
    
    while True:
        print ideone.getSubmissionStatus(link)

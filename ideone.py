from SOAPpy import WSDL


def createTuple(item):
    return (item['key'], item['value']) 

def createDict(items):
    ret = {}
    tuples = map(createTuple, items)
    for tuple in tuples:
        ret[tuple[0]] = tuple[1]
    return ret

class IdeOne:
    def __init__(self, user='test', password='test'):
        self._user = user
        self._password = password

        # creating wsdl client
        self._wsdlObject = WSDL.Proxy('http://ideone.com/api/1/service.wsdl')


    def getLanguages(self):
        """returns a list of tuples with languages supported by ideone"""
        response = self._wsdlObject.getLanguages(self._user, self._password)
        languages = response['item'][1]['value']['item']

        return map(createTuple, languages)

    def testFunction(self):
        """call ideone test function"""
        result = self._wsdlObject.testFunction('test', 'test')
        items = result['item']
        return createDict(items)


if __name__ == "__main__":
    ideone = IdeOne()
    print ideone.getLanguages()
    print ideone.testFunction()

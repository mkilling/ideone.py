from SOAPpy import WSDL

class IdeOne:
    def __init__(self, user='test', password='test'):
        self._user = user
        self._password = password

        # creating wsdl client
        self._wsdlObject = WSDL.Proxy('http://ideone.com/api/1/service.wsdl')

    def getLanguages(self):
        """returns a list of tuples with languages supported by ideone"""
        response = self._wsdlObject.getLanguages(self._user, self._password)
        languages = response[0][1][1][0]

        print response['item']

        createTuple = lambda l: (l['key'], l['value']) 
        return map(createTuple, languages)

    def testFunction(self):
        """call ideone test function"""
        result = self._wsdlObject.testFunction('test', 'test')


if __name__ == "__main__":
    ideone = IdeOne()
    ideone.getLanguages()

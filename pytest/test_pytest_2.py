import requests

"""Execute o teste da aplicação com pytest (pytest 'Nome no seru arquivo .py')'"""
class TestExample:

    def consume_api(self, method):
        url = 'http://apitestexcapital.herokuapp.com/api/v1/user/'
        response = requests.request(method, url)
        if response:
            return response.status_code
        
    def mult(self, x, y):
        return x * y

    def somar(self,x , y):
        return x + y

    def test_somar(self):
        assert self.somar(10, 20) == 30

    def test_ult(self):
        assert self.mult(2, 3) == 6

    def test_one(self):
        linguage = 'python'
        assert 'py' in linguage
    
    def test_two(self):
        assert 10 == 10

    def test_api(self):
        assert self.consume_api('GET') == 200
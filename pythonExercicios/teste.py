from requests import get
resp = get('http://www.pudim.com.br/')
if resp:
    print('ok')
else:
    print('Falhou')

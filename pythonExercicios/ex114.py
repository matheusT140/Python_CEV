# import requests # (Essa biblioteca precisou ser instalada)
from urllib import request, error
print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 114', '-' * 33)
print('-' * 25, 'Função - Site está acessível?', '-' * 26)
print('=-' * 41)
#   Solução usando a biblioteca requests
#    try:
#       resp = requests.get('http://www.pudim.com.br/')
#    except requests.ConnectionError:
#        print('\033[31mO site Pudim não está acessível no momento\033[m')
#    else:
#        print('\033[33mConsegui acessar o site Pudim com sucesso.\033[m')
try:
    resp = request.urlopen('http://www.pudim.com.br/')
except error.URLError:
    print('\033[31mO site Pudim não está acessível no momento\033[m')
else:
    print('\033[33mConsegui acessar o site Pudim com sucesso.\033[m')


import urllib
import urllib.request


try:
    site = urllib.request.install_opener('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu erro')
else:
    print('Acesso concebido')

import requests


def test_conn(tt_url):
    r = requests.get(tt_url)
    if r.status_code == 200:
        return print('Conexão com o website estável.')
    return print('Conexão com o website instável.')

'kkcoding-cli - Command-line Interface for KKCoding.net'

import getpass
import json

import requests


def login(username, password):
    'Login with username and password'
    return json.loads(requests.post('http://www.kkcoding.net/thrall-web/user/login',
                                    json={'name': username, 'password': password}).text)

def main():
    "__name == '__main__'"
    res = login(input('Username: '), getpass.getpass())
    if not res['data']:
        raise Exception(res['msg'])
    user = res['data']
    token = user['ticket']
    print(token)

if __name__ == '__main__':
    main()

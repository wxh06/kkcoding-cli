'kkcoding-cli - Command-line Interface for KKCoding.net'

import getpass
import json
import os
import sys

import requests


def login(username, password):
    'Login with username and password'
    return json.loads(requests.post('http://www.kkcoding.net/thrall-web/user/login',
                                    json={'name': username, 'password': password}).text)

def main(args):
    "__name == '__main__'"
    confdir = os.path.join(os.path.expanduser('~'), '.kkcoding')
    os.makedirs(confdir, exist_ok=True)
    if args[0] == 'login':
        res = login(input('Username: '), getpass.getpass())
        if not res['data']:
            raise Exception(res['msg'])
        user = res['data']
        token = user['ticket']
        with open(os.path.join(confdir, 'token.txt'), 'w') as file:
            file.write(token)
    elif args[0] == 'logout':
        os.remove(os.path.join(confdir, 'token.txt'))
    else:
        token = open(os.path.join(confdir, 'token.txt')).read()

if __name__ == '__main__':
    main(sys.argv[1:])

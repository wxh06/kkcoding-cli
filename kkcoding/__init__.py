'kkcoding-cli - Command-line Interface for KKCoding.net'

import argparse
import getpass
import json
import os
import sys

import requests

__version__ = '0.0.1'


def login(name: str, password: str) -> dict:
    'Login with the given username and password'
    return json.loads(requests.post('http://www.kkcoding.net'
                                    '/thrall-web/user/login',
                                    json={'name': name,
                                          'password': password}).text)


def daily_sign(token: str) -> dict:
    'Daily sign'
    return json.loads(requests.get('http://www.kkcoding.net'
                                   '/thrall-web/sign/dailySign',
                                   headers={'token': token}).text)


def main(*argv: list):
    "__name == '__main__'"
    parser = argparse.ArgumentParser('kkcoding')
    parser.add_argument('--config-dir', nargs='?',
                        default=os.path.join(os.path.expanduser('~'),
                                             '.kkcoding'))
    subparsers = parser.add_subparsers(dest='command',
                                       required=True, help='Command')
    parser_login = subparsers.add_parser('login', help=login.__doc__)
    parser_login.add_argument('name', nargs='?',
                              default='', help='Your username')
    subparsers.add_parser('logout', help='Logout')
    subparsers.add_parser('sign', help='Daily sign')
    args = parser.parse_args(argv)
    confdir = args.config_dir
    os.makedirs(confdir, exist_ok=True)
    open(os.path.join(confdir, 'token.txt'), 'a').close()
    if args.command == 'login':
        res = login(args.name or input('Username: '), getpass.getpass())
        if res['code'] != 200:
            raise Exception(res['msg'])
        if res['msg']:
            print(res['msg'])
        token = res['data']['ticket']
        with open(os.path.join(confdir, 'token.txt'), 'w') as file:
            file.write(token)
    elif args.command == 'logout':
        os.remove(os.path.join(confdir, 'token.txt'))
    elif args.command == 'sign':
        token = open(os.path.join(confdir, 'token.txt')).read()
        try:
            res = daily_sign(token)
        except json.decoder.JSONDecodeError:
            raise Exception('登录信息过期,请重新登录!')
        if res['code'] != 200:
            raise Exception(res['msg'])
        if res['msg']:
            print(res['msg'])


def console():
    main(*sys.argv[1:])


if __name__ == '__main__':
    console()

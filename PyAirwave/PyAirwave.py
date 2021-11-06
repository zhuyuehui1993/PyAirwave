# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@author: zhuyuehui
@contact: zhuyuehui02@meituan.com
@time: 2021/11/6 10:53 上午
"""

import requests
import urllib3

urllib3.disable_warnings()


class AirWaveError(Exception):
    pass


class AirWave:
    """
    https://support.hpe.com/hpesc/public/docDisplay?docId=a00046588en_us&docLocale=en_US
    根据官网提供文档改写。

    e.g:
        aw = AirWave('login', 'passwd', '192.168.1.1')
        res = aw.get_clients('zhuyuehui')
    """
    cookie = None
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    def __init__(self, username, password, host):
        self.credential_0 = username
        self.credential_1 = password
        self.host = host
        self.domain = f'https://{host}'
        self.login()

    def _add_token(self, token):
        self.headers['X-BISCOTTI'] = token

    def login(self):
        url = '/LOGIN'
        data = {
            'credential_0': self.credential_0,
            'credential_1': self.credential_1,
            'login': 'Log in',
            'destination': '/'
        }

        rp = requests.post(f'{self.domain}{url}', headers=self.headers, data=data, verify=False)
        if rp.status_code != 200:
            raise AirWaveError('获取cookie，token 失败。')

        h = rp.history[0].headers
        self._add_token(h['X-BISCOTTI'])
        self.cookie = {'MercuryAuthHandlerCookie_AMPAuth': h['Set-Cookie'].split('=')[1].split(';')[0]}

    def get_clients(self, name):
        uri = '/api/search.json'
        parameter = {
            'query': name,
        }
        rq = requests.get(f'{self.domain}{uri}', headers=self.headers, params=parameter, cookies=self.cookie,
                          verify=False)
        if rq.status_code != 200:
            raise AirWaveError('获取用户信息失败！')

        return rq.json()


if __name__ == '__main__':
    aw = AirWave('login', 'passwd', '192.168.1.1')
    res = aw.get_clients('zhuyuehui')

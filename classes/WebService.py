#!/usr/bin/env python
import requests


class WebService:

    def __init__(self, url):
        self.url = url

    def log_pump(self, msg):

        print('POST WebService - ')
        print(msg)
        print('- POST END')

        r = requests.post(self.url + '/log', json=msg)
        print(r.text)
        return r

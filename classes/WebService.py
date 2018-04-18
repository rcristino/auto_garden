#!/usr/bin/env python
import requests


class WebService:

    def __init__(self, url):
        self.url = url

    def log_pump(self, msg):
        r = requests.post(self.url + '/log', msg)
        return r.text

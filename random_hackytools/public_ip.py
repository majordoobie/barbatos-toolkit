#!/usr/bin/python3
from requests import get
ip = get('https://api.ipify.org').text
print('My exit node is: {}'.format(ip))

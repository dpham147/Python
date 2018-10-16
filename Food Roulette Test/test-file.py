
from __future__ import print_function

from yelp.client import Client

import argparse
import json
import pprint
import requests
import sys
import urllib
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode

API_KEY = 'cpIVlz8OLRcLoz-Wwut-tJxohNcOV7z_uInTckHuYOFQc2WALNDYJY0BKSo01kGNjA_sUBt3s4wIi2shzJO3Lc_Dj8RrcWA8agL7N0B0R9-NOhdADQX81uCT-W_W3Yx'

header = {'Authorization': 'Bearer %s' % API_KEY}
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
param = {'term': 'steak', 'location': 'New York City, NY', 'limit': 3}

client = Client(API_KEY)

url = '{0}{1}'.format(API_HOST, quote(SEARCH_PATH.encode('utf8')))
response = requests.request('GET', url, headers=header, params=param)
response = response.json()
print(response)


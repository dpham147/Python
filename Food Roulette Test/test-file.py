from __future__ import print_function
from yelp.client import Client
import json
import pprint
import requests
import sys
import urllib
# noinspection PyCompatibility
from urllib.parse import quote

# API Key
API_KEY = 'cpIVlz8OLRcLoz-Wwut-tJxohNcOV7z_uInTckHuYOFQc2WALNDYJY0BKSo01kGNjA_sUBt3s4wIi2shzJO3Lc_Dj8RrcWMA8agL7N0B0R9-NOhdADQX81uCT-W_W3Yx'


# API constants
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'

# Default search terms
DEFAULT_TERM = 'lunch'
DEFAULT_LOCATION = 'Fullerton, CA'
DEFAULT_LIMIT = 10


def search(api_key, term, location, limit):
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': limit
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def request(host, path, api_key, url_params=None):
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {'Authorization': 'Bearer %s' % api_key}

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def get_business(api_key, business_id):
    business_path = BUSINESS_PATH + business_id
    return request(API_HOST, business_path, api_key)


def query_api(term, location, limit):
    response = search(API_KEY, term, location, limit)

    businesses = response.get('businesses')

    if not businesses:
        print(u'No businesses for {0} in {1} found.'.format(term, location))
        return

    business_id = businesses[0]['id']

    print(u'{0} businesses found, querying business info ' \
          'for the top result "{1}" ...'.format(
        len(businesses), business_id))
    response = get_business(API_KEY, business_id)

    print(u'Result for business "{0}" found:'.format(business_id))
    pprint.pprint(response, indent=2)
'''
    business_id = {}
    for business in range(len(businesses)):
        business_id[business] = businesses[business]['id']

    print(u'{0} businesses found, querying business info for top 5 results ...'
          .format(len(businesses)))

    for id in business_id:
        response = get_business(API_KEY, id)

        print(u'Result for business "{0}" found:'.format(id))
        pprint.pprint(response, indent=2)
'''

query_api(DEFAULT_TERM, DEFAULT_LOCATION, DEFAULT_LIMIT)




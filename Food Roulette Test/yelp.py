from __future__ import print_function
import pprint
import requests
try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib import HTTPError
    from urllib import quote
    from urllib import urlencode

# API Key
API_KEY = 'cpIVlz8OLRcLoz-Wwut-tJxohNcOV7z_uInTckHuYOFQc2WALNDYJY0BKSo01kGNjA_sUBt3s4wIi2shzJO3Lc_Dj8RrcWMA8agL7N0B0R9-NOhdADQX81uCT-W_W3Yx'

# API constants
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'


def query_api(term, location, limit):
    """
    Queries the Yelp API and returns a JSON of business info
    :param term: Query Term
    :param location: Query Location
    :param limit: Maximum number of results
    :return: A Dictionary of businesses found
    """

    response = __search__(API_KEY, term, location, limit)
    businesses = response.get('businesses')
    business_dict = {}

    # If no businesses were found
    if not businesses:
        print(u'No businesses for {0} in {1} found.'.format(term, location))
        return

    # Add businesses to a dictionary
    for business in businesses:
        business_dict[business['id']] = business

    return business_dict


def find_business_by_id(business_id):
    """
    Find a specific business's info given an ID
    :param business_id: A business's ID
    :return: Dictionary of business info
    """
    return __get_business__(API_KEY, business_id)


def print_info(business):
    """
    Prints the Python Dictionary of business information
    Use this to print information to console
    :param business: A Dictionary of a specific business
    :return: NONE
    """
    pprint.pprint(business, indent=2)


def print_info_dump(business_dict):
    """
    Prints the Python Dictonary of a dictionary of businesses
    :param business_dict: The dictionary to print
    :return: NONE
    """
    for business in business_dict:
        print_info(business_dict[business])


def __search__(api_key, term, location, limit):
    """
    Prepares the search queries for HTTP request
    :param api_key: Yelp Fusion API Key
    :param term: Query Term
    :param location: Query Location
    :param limit: Maximum number of results
    :return: A JSON of businesses queried
    """
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': limit
    }
    return __request__(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def __request__(host, path, api_key, url_params=None):
    """
    Sends a HTTP request to Yelp for businesses
    :param host: API Host domain
    :param path: API Search Path
    :param api_key: Yelp Fusion API Key
    :param url_params: Request parameters
    :return: A JSON of businesses
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {'Authorization': 'Bearer %s' % api_key}

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def __get_business__(api_key, business_id):
    """
    Returns a Dictionary of business info
    :param api_key: Yelp Fusion API Key
    :param business_id: Unique ID of a business
    :return: Dictionary containing business info
    """
    return __request__(API_HOST, BUSINESS_PATH + business_id, api_key)


##################### TEST FUNCTIONS ####################
print('------------PRINTING INFO BY ID------------')
print_info(find_business_by_id('w6T-6l8_zKeYMtaokW1zVg'))
print('-----------PRINTING 10 BOBA SHOPS IN FULLERTON------------')
print_info_dump(query_api('boba', 'fullerton, ca', 10))
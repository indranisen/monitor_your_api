import requests
import xml.etree.ElementTree as ET
import netrc
__author__='Indrani Sen'

api_endpoint = 'https://maps.googleapis.com/maps/api/directions/xml?origin=Toronto&destination=Montreal&key='


def get_api_key(app):
    try:
        info = netrc.netrc()
        api_id, account, api_key = info.authenticators(app)
    except IOError:
        print 'no authentication details loaded'
        quit()
    except netrc.NetrcParseError:
        print 'no authentication details loaded'
        quit()
    except TypeError:
        print 'no authentication details loaded'
        quit()
    return api_key


def return_api_endpoint(app):
    return api_endpoint+get_api_key(app)


def get_request(app):
    endpoint = api_endpoint+get_api_key(app)
    actual_response = requests.get(endpoint)
    return _return_response_status_code(actual_response), _return_response_headers(actual_response), \
        _return_response_content(actual_response), _return_content_type_header_field(actual_response)


def _return_response_headers(response_object):
    return response_object.headers


def _return_response_status_code(response_object):
    return response_object.status_code


def _return_response_content(response_object):
    return response_object.content


def _return_content_type_header_field(response_object):
    return _return_response_headers(response_object)['Content-Type']


def _return_content_length_header_field(response_object):
    return _return_response_headers(response_object)['Content-Length']



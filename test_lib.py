__author__='Indrani Sen'

import requests
import xml.etree.ElementTree as ET
import netrc

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
    return api_endpoint+get_api_key('google-map-directions')

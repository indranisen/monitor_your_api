__author__='Indrani Sen'
import test_lib as lib

response_status_code, response_headers, response_content = lib.get_request('google-map-directions')
print response_status_code
print response_headers


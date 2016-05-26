import monitor_your_api.test_lib as lib
__author__='Indrani Sen'

response_status_code, response_headers, response_content, content_type = lib.get_request('google-map-directions')
print response_status_code
print response_headers
print content_type


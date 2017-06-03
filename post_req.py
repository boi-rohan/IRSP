# install requests first :P
import requests

def post_req(username, password, court_pk, value, url):
    requests.post(url + 'api/post_datetimevalue/',
    				# court_pk - int; value - Boolean 
    				data={'court':court_pk, 'value':value}, 
    				# username; password - strings
    				auth = (username, password)
    				)
    return
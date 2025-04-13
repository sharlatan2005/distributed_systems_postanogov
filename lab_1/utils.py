from urllib.parse import urlencode, urlunparse, urlparse
from config import AUTH_URL, CLIENT_ID, REDIRECT_URL
import webbrowser 

def get_url_with_query_params(base_url, params):
    url_parts = list(urlparse(base_url))
    url_parts[4] = urlencode(params)
    final_url = urlunparse(url_parts)

    return final_url

def redirect_to_auth_url():
    query_params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URL,
        'prompt': 'consent'
    }

    auth_url = get_url_with_query_params(AUTH_URL, query_params)
    webbrowser.open(auth_url)
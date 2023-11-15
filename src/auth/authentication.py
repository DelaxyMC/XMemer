from requests_oauthlib import OAuth1Session
from src.auth import keys

api_key = keys.api_key


# Make the request
def get_oauth():
    oauth = OAuth1Session(
        keys.api_key,
        client_secret=keys.api_key_secret,
        resource_owner_key=keys.access_token,
        resource_owner_secret=keys.access_token_secret,
    )
    return oauth

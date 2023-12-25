import requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

def get_access_token(client_id, client_secret, tenant_id):
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    scope = ["https://graph.microsoft.com/.default"]

    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=token_url, client_id=client_id,
                              client_secret=client_secret, scope=scope)

    return token['access_token']


def get_file_id(access_token, site_id, library_name):
    url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{library_name}/items?expand=fields(select=id,Title,FileRef)"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        items = response.json().get('value')
        for item in items:
            # Assuming you're looking for a file by its name
            if item['fields']['Title'] == 'YourFileName':
                return item['fields']['id']
    else:
        print(f"Error: {response.status_code}")
        return None

# Usage
client_id = 'a1dccbc1-bba2-4269-9039-a7297fd095d6'
client_secret = 'Z6M8Q~QQ9j3kn4QOhIifo~RYjx~I~nFb65PDbcX0'
tenant_id = '8133ead4-1b34-4a4f-aab5-2f0cdf410e8c'
site_id = 'd5129c9b-3a1e-47c7-af54-1b7b96106ae7,59fc2ce4-1369-446c-bd14-e111a283eb9a'
library_name = 'Documents'

access_token = get_access_token(client_id, client_secret, tenant_id)
file_id = get_file_id(access_token, site_id, library_name)

if file_id:
    print(f"File ID: {file_id}")
else:
    print("File not found or error occurred.")

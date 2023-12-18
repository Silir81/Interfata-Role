from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

# SharePoint site URL
site_url = 'https://mexiweb.sharepoint.com/sites/MF40'

# Application (client) ID and client secret from your Azure AD app
client_id = "95c8995b-9aa0-41b2-a714-7a3105b5d8dc"
client_secret = "7Fq8Q~aidcruzEO96KLY642eNDvaT6Mh3TEQkbPr"

# Create an authentication context
context_auth = AuthenticationContext(url=site_url)

# Acquire token for app
context_auth.acquire_token_for_app(client_id=client_id, client_secret=client_secret)

# Create a client context
ctx = ClientContext(site_url, context_auth)

# Load the web object
web = ctx.web
ctx.load(web)
ctx.execute_query()

# Print the web site title
print("Web site title: {0}".format(web.properties['Title']))

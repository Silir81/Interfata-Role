from msal import ConfidentialClientApplication
from msgraph.core import GraphSession, Credential

# Application (client) ID, tenant ID, and client secret from your AAD app
CLIENT_ID = "95c8995b-9aa0-41b2-a714-7a3105b5d8dc"
TENANT_ID = "8133ead4-1b34-4a4f-aab5-2f0cdf410e8c"
CLIENT_SECRET = "71e38eec-0849-4803-b550-afd2404873c8"

# SharePoint site URL and file path
site_url = "https://mexiweb.sharepoint.com/sites/MF40"
file_relative_url = "sites/MF40/Documente%20partajate/Stoc%20Role/Stoc%20Role%202022%20-%20Test.xlsx"

# Build the authority URL
authority_url = f"https://login.microsoftonline.com/{TENANT_ID}"

# Create a confidential client application
app = ConfidentialClientApplication(
    client_id=CLIENT_ID,
    authority=authority_url,
    client_credential=CLIENT_SECRET
)

# Get the access token
token_response = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
access_token = token_response.get("access_token")

# Initialize a Graph session with the access token
credential = Credential(access_token=access_token)
session = GraphSession(credential=credential)

# Download the file content
response = session.get(f"drives/b!m5wS1R46x0evVBt7lhBq5-Qs_FlpE2xEvRThEaKD65rYp5aXnZpSQ5Ngp-we3IN7/items/{item_id}/content")

# Save the file locally
if response.status_code == 200:
    with open("local_file.xlsx", "wb") as file:
        file.write(response.content)
        print("File downloaded successfully.")
else:
    print("File download failed. Status code:", response.status_code)

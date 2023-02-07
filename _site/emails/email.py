# Include the Sendinblue library\
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
# Instantiate the client\
sib_api_v3_sdk.configuration.api_key['api-key'] = 'YOUR_API_V3_KEY'
api_instance = sib_api_v3_sdk.EmailCampaignsApi()
# Define the campaign settings\
email_campaigns = sib_api_v3_sdk.CreateEmailCampaign(
name= "API",
subject= "CARHub",
sender= { "name": "From name", "email": "anshuman.kashyap@sendinblue.com"},
type= "classic",
# Content that will be sent\
html_content= "Congratulations! You successfully sent this example campaign via the Sendinblue API.",
# Select the recipients\
recipients= {"listIds": [2, 7]},
# Schedule the sending in one hour\
scheduled_at= "2018-01-01 00:00:01"
)
# Make the call to the client\
try:
api_response = api_instance.create_email_campaign(email_campaigns)
pprint(api_response)
except ApiException as e:
print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)
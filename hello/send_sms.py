# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC8ef56b14520c627f847567e3993f851d"
auth_token = "c6be7446d9f82b30070cfc0e4031a091"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+14168343783", from_="+16475600383",
                                     body="Hello there!")

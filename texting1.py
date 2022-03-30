from twilio.rest import Client

accountSID = 'AC3dce134ef0d682e6ce6c44a3aba838cb'

authToken = 'b0f22ef02ddaaa1f55fe33693ce70674'

client = Client(accountSID, authToken)

TwilioNumber = '+12672140922'

mycellphone = '+17327887622'


textmessage = client.messages.create(to  = mycellphone, from_= TwilioNumber, body ='Hello World!')


print(textmessage.status)


## make a phone call 

call = client.calls.create(url = "http://demo.twilio.com/docs/voice.xml", to = mycellphone, from_=TwilioNumber)
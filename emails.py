import win32com.client 
from twilio.rest import Client 

outlook = win32com.client.Dispatch("Outlook.Application")
outlook_ns = outlook.GetNamespace("MAPI")

myfolder = outlook_ns.Folders['nichol_vacca1@baylor.edu'].Folders['Inbox']

messages = myfolder.Items 

messagecount = 0 


'''
for message in messages:
    if message.UnRead == True: 
        print(message.sender) 
        print(message.subject)

        if 'absence' in message.subject: 
            print("Found message with absence")
            Msg = outlook.CreateItm(0)
            Msg.Importance = 1
            Msg.Subject = 'Got your ' + message.subject + 'email'
            Msg.HTMBody = 'Hi' + str(message.sender) + '\n' +', sorry you are not well'

            Msg.To = message.sender.GetExchangeUser().PrimarySmtpAddress
            Msg.ReadReceiptRequeted = True 

            Msg.Send()
'''

## send text of number of emails in inbox 

accountSID = 'AC3dce134ef0d682e6ce6c44a3aba838cb'
authToken = 'b0f22ef02ddaaa1f55fe33693ce70674'
client = Client(accountSID, authToken)
TwilioNumber = '+12672140922'
mycellphone = '+17327887622'

for message in messages: 
    messagecount += 1 

textmessage = client.messages.create(to  = mycellphone, from_= TwilioNumber, body ='messagecount: ' + str(messagecount))
print(textmessage.status)

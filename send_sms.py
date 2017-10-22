from twilio.rest import Client

def send_sms():
    # Your Account SID from twilio.com/console
    account_sid = "AC35e90ca10c7dbde842cf24872703f8d0"
    # Your Auth Token from twilio.com/console
    auth_token  = "6dfd1f58dfe4cf5d8cc57fafd96c2c3d"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+13105955397", 
        from_="+16193320748",
        body="Someone wants to connect with you on GenMatch.tech!")

    print(message.sid)

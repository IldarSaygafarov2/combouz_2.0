import http.client
import json
from combouz import settings


def send_sms_message(recipient, message: str):
    conn = http.client.HTTPSConnection(settings.SMS_HOST)
    
    payload = json.dumps({
        "messages": [
            {
                "destinations": [{"to": recipient}],
                "from": settings.SMS_SENDER,
                "text": message
            }
        ]
    })
    
    headers = {
        'Authorization': f'App {settings.SMS_API_KEY}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    conn.request("POST", "/sms/2/text/advanced", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

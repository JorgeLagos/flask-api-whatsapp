import requests
import json

def send_message_wsp(data):
    try:
        token = 'EAACMBtknV6EBAO5fmBGZCTQrpMxx5iNGz72pnMPZAyV2ZCXLIoZCzPoYaZBMNQz7pka37kyDsTZBZAIVf2XZCwMJUqjPZAZADfT2My4WZAOd6ns5hF0IPkxc9xotejpItvrQ3O0PYBhjFMjsHTRfOgJ1M5awygCeeV4hVu7OUxvCdNh9WluniGdLyEwrvqY5gjzJmcMCZBI3ULef1dJDC8VLbSxkAW9k89vPuJQZD'
        api_url = 'https://graph.facebook.com/v15.0/113189058361758/messages'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        response = requests.post(api_url, data=json.dumps(data), headers=headers)
        if (response.status_code == 200):
            return True
        return False
    except Exception as exception:
        print(exception)
        return False

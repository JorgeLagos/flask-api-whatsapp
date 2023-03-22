import requests
import json

def send_message_wsp(data):
    try:
        token = 'EAACMBtknV6EBACDKEQ79qba6BRAgnEDt54xDuOguaWThvBSvv79gu3tLZA1sxoGPlndMbtbyrCqFgKwxPLLgaGM9VT4hrIytqFQZC61I8a4yPXZBxOkXMteoNmjFeHeN22LwNejoNJ2fhB60jmZA4OrtftAcxFCZCwR6lYTVYSR5aLj7ZBSFNG1u2dIf8ZAMwUH4JbUZCFHNLx6gCbaAZBsFdLC5eMggFzo8ZD'
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

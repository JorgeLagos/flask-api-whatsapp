import requests
import json
import os

def send_message_wsp(data):
    try:
        token = os.getenv('WSP_API_TOKEN')
        api_url = os.getenv('WSP_API_URL')
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

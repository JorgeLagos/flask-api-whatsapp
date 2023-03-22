import requests
import json

def send_message_wsp(data):
    try:
        token = 'EAACMBtknV6EBAPWZB0yPk3dSqQIZCtW4DLJq7BBcA79W22Lu7tyM4D8vDe0ZAa7wRlNzuByrHZBjXq5guo8nNfalKhYxlWNg8kP6cHnN61v28geKp0kJxZCNXZCN7IRicn2G4myMpVTT05i1jau06prDWR84WHmuMyD1LKAZBofm9CXAHZCfWLZAgZCCMCecwqadZCB4pc4Ek06v1I6Tc6K4mtv3IHvEWiR4DEZD'
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

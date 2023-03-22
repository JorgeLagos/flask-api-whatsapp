import requests
import json

def send_message_wsp(data):
    try:
        token = 'EAACMBtknV6EBAINiUghub36TvS3Wt1HhFuZAlTTSOIZBmjzV5H8TSZByH8EzOPdNFcgfHIDlOhAdizEWUstVwnyoEcJMAbeaDhODNIQFK7F0RZBEgUvl1kALVK8n0OSYTFaJoLgNqo0blFU54OlZCHZBe2GrmcltBk56kv0LiEozKfSAjwZCHfWWrppjTHkFGVsWvly5jf5bVqkQIsGYmkUk1fED414nf4ZD'
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

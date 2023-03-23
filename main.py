import os

from flask import Flask, request
from dotenv import load_dotenv

import util
import services

app = Flask(__name__)

load_dotenv()

@app.route('/welcome', methods=['GET'])
def index():
    return 'Welcome dev'

@app.route('/whatsapp', methods=['GET'])
def verify_token():
    try:
        access_token = 'ffKsdfDGdfsfHVfsdG5B6H5sgb'
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if (token != None and challenge != None and token == access_token):
            return challenge
        else:
            return '', 400
    except:
        return '', 400

@app.route('/whatsapp', methods=['POST'])
def received_message():
    try:
        body = request.get_json()
        entry = body.get('entry')[0]
        changes = entry.get('changes')[0]
        value = changes.get('value')
        messages = value.get('messages')[0]
        from_number = messages.get('from')

        message = util.get_message_user(messages)
        # send_message(message, from_number)
        process_message(message, from_number)

        return 'EVENT_RECEIVED'
    except:
        return 'EVENT_RECEIVED'
    
def process_message(text, phone):
    text = text.lower()
    list_data = []

    if 'hi' in text: 
        data = util.message_type_text('Hello, how can i help you?', phone)
        data_menu = util.message_type_list(phone)
        list_data.append(data)
        list_data.append(data_menu)

    elif 'thank' in text: 
        data = util.message_type_text('Thank you for contacting me', phone)

    elif 'agency' in text:
        data = util.message_type_text('This is our agency', phone)
        data_location = util.message_type_location(phone)
        list_data.append(data)
        list_data.append(data_location)
    
    elif 'contact' in text:
        data = util.message_type_text('*Contact Center:*\n+56963230969', phone)
        list_data.append(data)

    elif 'buy' in text:
        data = util.message_type_buttons(phone)
        list_data.append(data)

    elif 'sell' in text:
        data = util.message_type_buttons(phone)
        list_data.append(data)

    elif 'sing up' in text:
        data = util.message_type_text('Enter this link to register: https://form.jotform.com/222507994363665', phone)
        list_data.append(data)
    
    elif 'log in' in text or 'login' in text:
        data = util.message_type_text('Enter this link to login: https://form.jotform.com/222507994363665', phone)
        list_data.append(data)

    else: 
        data = util.message_type_text('Im sorry, i cant understand you', phone)
        list_data.append(data)

    for item in list_data:
        services.send_message_wsp(item)

def send_message(text, phone):
    text = text.lower()
    if 'text' in text: data = util.message_type_text('Text', phone)
    if 'format' in text: data = util.message_type_text_format(phone)
    if 'image' in text: data = util.message_type_image(phone)
    if 'audio' in text: data = util.message_type_audio(phone)
    if 'video' in text: data = util.message_type_video(phone)
    if 'document' in text: data = util.message_type_document(phone)
    if 'location' in text: data = util.message_type_location(phone)
    if 'buttons' in text: data = util.message_type_buttons(phone)
    if 'list' in text: data = util.message_type_list(phone)
    services.send_message_wsp(data)

if (__name__ == '__main__'):
    app.run(debug=True, port=os.getenv('PORT', default=5000))

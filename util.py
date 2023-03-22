def get_message_user(message):
    text_msg = None
    type_msg = message.get('type')
    if (type_msg == 'text'):
        text_msg = message.get('text').get('body')
    elif (type_msg == 'interactive'):
        interactive = message.get('interactive')
        type_interactive = interactive.get('type')
        if (type_interactive == 'button_reply'):
            text_msg = interactive.get('button_reply').get('title')
        else:
            text_msg = interactive.get('list_reply').get('title')
    else:
        print('Sin message')
    return text_msg

def message_type_text(text, number):
    data = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': number,
        'type': 'text',
        'text': {
            'body': text
        }
    }
    return data

def message_type_text_format(number):
    data = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': number,
        'type': 'text',
        'text': {
            'body': 'Hola mundo, *Hola mundo*, _Hola mundo_, ~Hola mundo~, ````Hola mundo```'
        }
    }
    return data

def message_type_image(number):
    data = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': number,
        'type': 'image',
        'image': {
            'link': 'https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/image_whatsapp.png'
        }
    }
    return data

def message_type_audio(number):
    data = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': number,
        'type': 'audio',
        'audio': {
            'link': 'https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/audio_whatsapp.mp3'
        }
    }
    return data

def message_type_video(number):
    data = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': number,
        'type': 'video',
        'video': {
            'link': 'https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/video_whatsapp.mp4',
            'caption': 'Your Video'
        }
    }
    return data

def message_type_document(number):
    data = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': number,
        'type': 'document',
        'document': {
            'link': 'https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/document_whatsapp.pdf',
            'caption': 'Your Document'
        }
    }
    return data

def message_type_location(number):
    data = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': number,
        'type': 'location',
        'location': {
            'latitude': '-33.46456539306906',
            'longitude': '-70.61064429606428',
            'name': 'Estadio Nacional',
            'address': 'Av. Grecia 2001, Ñuñoa, Región Metropolitana'
        }
    }
    return data

def message_type_buttons(number):
    data = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': number,
        'type': 'interactive',
        'interactive': {
            'type': 'button',
            'body': {
                'text': 'Do you already have an account? 🫡'
            },
            'action': {
                'buttons': [
                    {
                        'type': 'reply',
                        'reply': {
                            'id': 'btn_001',
                            'title': 'Sign up'
                        }
                    },
                    {
                        'type': 'reply',
                        'reply': {
                            'id': 'btn_002',
                            'title': 'Log in'
                        }
                    }
                ]
            }
        }
    }
    return data

def message_type_list(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "✅ I have these options"
            },
            "footer": {
                "text": "Select an option"
            },
            "action": {
                "button": "See options",
                "sections": [
                    {
                        "title": "Buy and sell products",
                        "rows": [
                            {
                                "id": "main-buy",
                                "title": "Buy",
                                "description": "Buy the best product your home"
                            },
                            {
                                "id": "main-sell",
                                "title": "Sell",
                                "description": "Sell your products"
                            }
                        ]
                    },
                    {
                        "title": "📍center of attention",
                        "rows": [
                            {
                                "id": "main-agency",
                                "title": "Agency",
                                "description": "Your can visit our agency"
                            },
                            {
                                "id": "main-contact",
                                "title": "Contact center",
                                "description": "One of our agents will assist you"
                            }
                        ]
                    }
                ]
            }
        }
    }
    return data



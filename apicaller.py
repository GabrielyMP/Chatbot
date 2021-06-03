# Antes de rodar, instalem essa biblioteca 
import requests

def get_location_for_key(search_text, coordinates = None) :
    # Constantes
    MAIN_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    PLACE_ID_URL = "https://maps.googleapis.com/maps/api/place/details/json"
    KEY = "AIzaSyBLuoVGkFGk7mc25W55H4ajG3IKT0iOeWg"

    # Parâmetros da chamada á API
    PARAMS = {
        'key': KEY,
        'input': search_text,
        'inputtype': 'textquery'
    }

    if coordinates:
        PARAMS['locationbias'] = f'circle:20000@{coordinates["latitude"]},{coordinates["longitude"]}'

    # Fazendo a chamada á API
    r = requests.get(url = MAIN_URL, params = PARAMS)

    # Resposta JSON da chamada
    data = r.json()

    place_id = data['candidates'][0]['place_id']

    PARAMS = {
        'key': KEY,
        'place_id': place_id,
    }

    # Fazendo a chamada á API
    r = requests.get(url = PLACE_ID_URL, params = PARAMS)

    # Resposta JSON da chamada
    data = r.json()
    return data['result']

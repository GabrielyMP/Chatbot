# Antes de rodar, instalem essa biblioteca 
import requests

def get_location_for_key(search_text) :
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
    place_data = data['result']
    print("Informações sobre o local:")
    print("Nome: {}".format(place_data['name']))
    print("Endereço: {}".format(place_data['formatted_address']))
    print("Tipo: {}".format(place_data['types']))
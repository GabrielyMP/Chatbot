from os import getcwd, path, remove
from random import choice
from re import search, IGNORECASE

from apicaller import get_location_for_key


chatbot_greetings_keys = [
    'Olá', 'Ola', 'Oi', 'Saudações', 'Saudacoes', 'Saudaçoes', 'Saudacões', 'Bom dia', 'Boa tarde',
    'Hello there', 'Eae', 'Iai', 'Eai', 'Iae', 'Yo'
]


chatbot_food_types_keys = [
    'japonesa', 'chinesa', 'tailandesa', 'mexicana', 'brasileira', 'francesa', 'fast food'
]


chatbot_food_names_by_type = {
    'japonesa': [
        'Sushi', 'Takoyaki', 'Toriyaki', 'Ramen', 'Yakisoba', 'Yakissoba', 'Okonomiyaki', 'Sashimi',
        'Tempura', 'Guioza', 'Temaki', 'Missoshiru', 'Huramaki', 'Sunomono', 'Gohan'
    ],
    'chinesa': [
        'Yakisoba', 'Yakissoba', 'Frango Xadrez', 'Tofu', 'Chop Suey'
    ],
    'tailandesa': [
        'Pad Thai', 'Tom Yum', 'Som Tam', 'Khao Soi', 'Tom Kha Gai', 'Massaman Curry', 'Shabu-shabu',
        'Yakiniku', 'Arroz Frito'
    ],
    'mexicana': [
        'Tortilla', 'Burrito', 'Taco', 'Nacho', 'Guacamole', 'Mixiote', 'Chilli con carne', 'Alegría',
        'Alegria', 'Polvoron', 'Polvorón', 'Garapiñados', 'Garapinados'
    ],
    'brasileira': [
        'Feijoada', 'Moqueca', 'Pão de Queijo', 'Carne de sol', 'Acarajé', 'Acaraje', 'Pao de Queijo',
        'Tapioca', 'Tacaca', 'Tacacá', 'Açai', 'Acai', 'Churrasco', 'Tainha na Taquara', 'Barreado',
        'Arroz com Pequi', 'Pintado à Urucum', 'Pintado a Urucum', 'Caldo de Piranha', 'Pudim de Leite',
        'Brigadeiro', 'Cocada'
    ],
    'francesa': [
        'Ratatouille', 'Creme brûlée', 'Creme brulee', 'Creme brûlee', 'Creme brulée', 'Macarons',
        'Cassoulet', 'Boeuf bourguignon'
    ],
    'fast food': [
        'Hamburguer', 'Burger', 'French Fries', 'Batata Frita', 'Sanduíche', 'Pizza', 'Donuts',
        'Frango Frito', 'Kebab'
    ],
}


chatbot_exit_keys = [
    'Tchau', 'Exit', 'Sair', 'Cancelar', 'Nao quero', 'Não quero'
]


chatbot_on_greetings_text = "Olá, humano. Eu me chamo Namaria e sou uma assistente virtual.\
    Quero ajudar você a encontrar os melhores restaurantes de acordo com o seu gostinho. Podemos começar? \
    Primeiramente, eu preciso saber de que tipo de comida você gosta... \
    Quer me contar um pouco mais sobre?"


chatbot_on_food_types_text_list = [
    "Hmmmmm. Então você gosta de comida {}, né? Tem razão. É bem deleitoso!"
]


chatbot_on_food_name_text_list = [
    "{}!? Eu também amo!"
]


chatbot_ask_user_coordinates = "Contudo, para encontrar o restaurante mais próximo de você, \
    preciso que você me forneça as suas coordenadas. Me faria a gentileza?"


chatbot_on_exit_text = "Tudo bem. Estou aqui se você precisar!"


def search_answer_by_key(user_message: str, coordinates: dict = None):
    answer = None

    for key in chatbot_greetings_keys:
        match = search(f'.*{key}.*', user_message, IGNORECASE)

        if not match: continue        

        answer = chatbot_on_greetings_text
    
    for key in chatbot_exit_keys:
        match = search(f'.*{key}.*', user_message, IGNORECASE)

        if not match: continue

        answer = chatbot_on_exit_text

    for key in chatbot_food_types_keys:
        match = search(f'.*{key}.*', user_message, IGNORECASE)

        if not match: continue

        answer = choice(chatbot_on_food_types_text_list).format(key)
        answer += " Aqui vai algumas sugestões pra você.\n"

        for food_name in chatbot_food_names_by_type[key]:
            answer += food_name + '\n'

    food_name_file_path = path.join(getcwd(), 'food_name.txt')

    for key in chatbot_food_names_by_type.keys():
        for food_name in chatbot_food_names_by_type[key]:
            match = search(f'.*{food_name}.*', user_message, IGNORECASE)

            if not match: continue

            answer = choice(chatbot_on_food_name_text_list).format(food_name)
            answer = answer + ' ' + chatbot_ask_user_coordinates

            try:
                with open(food_name_file_path, 'w') as file:
                    file.write(food_name)
            except IOError:
                print('Could not write on txt file')

            return answer

    if path.exists(food_name_file_path):
        food_name = None
        try:
            with open(food_name_file_path, "r") as file:
                food_name = file.read()
        except IOError:
            print("Could not read food name txt")
            
        if food_name != '':
            for option in ['Sim', 'Nao', 'Não']:
                match = search(f'.*{option}.*', user_message, IGNORECASE)

                if not match: continue

                if option == 'Sim':
                    answer = "BUSCAR COORDENADAS"
                    return answer
    
    if path.exists(food_name_file_path):
        food_name = None
        try:
            with open(food_name_file_path, "r") as file:
                food_name = file.read()
        except IOError:
            print("Could not read food name txt")

        if food_name != '':
            result = get_location_for_key(food_name, coordinates)
            name, address = result['name'], result['formatted_address']

            answer = "Achei um restaurante interessante pra você. Ele se chama {0}. Fica na {1}. Bon appetit!".format(name, address)

            try:
                with open(food_name_file_path, 'w') as file:
                    file.write('')
            except IOError:
                print('Could not write on txt')

    return answer


def process_user_message(user_message: str, coordinates: dict = None) -> str:
    bot_answer = ''

    try:
        bot_answer = search_answer_by_key(user_message, coordinates)
        assert bot_answer is not None
    except Exception as error:
        print(error)
        bot_answer = 'Não entendi o que você disse...'

    return bot_answer

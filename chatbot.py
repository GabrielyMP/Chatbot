# Seguinte, a merda do Chatterbot precisava de muito treinamento pra não ficar soltando umas frases nada a ver no meio da conversa, então foda-se, vamo fazer na mão msm. 
# Mas rlx que é parada simples, A gente tem só que desenvolver um diálogo bacaninha aqui, a idéia é conseguir pegar uma palavra chave nas respostas do usuário
# por exemplo: hambúrguer, sanduíche, sushi, esse tipo de coisa, a partir dessa palavra chave a gente vai usar a API do Google Places pra ele indicar um local de Manaus e pronto.
# sintam-se a vontade pra desenvolver melhor isso daí, pq esse diálogo tá uma bosta

import random
import re
from apicaller import get_location_for_key


def read_foods():
    foods = []
    try:
        with open('foods.txt', 'r') as file:
            foods = [food.rstrip() for food in file.readlines()]
    except IOError:
        print("Could not open foods txt file")
    return foods


def read_chatbot_answers():
    answers = []
    try:
        with open('chatbot.txt', 'r') as file:
            answers = [answer.rstrip() for answer in file.readlines()]
    except IOError:
        print("Could not open chatbot answers txt file")
    return answers


def search_answer_by_message(message: str) -> str:
    message = message.rstrip()

    foods = read_foods()
    for food in foods:
        if food in [word.lower() for word in message.split(' ')]:
            return food
    
    chatbot_answers = read_chatbot_answers()
    for answer in chatbot_answers:
        for word in answer.split(' '):
            for word2 in message.split(' '):
                if word == word2.lower():
                    return answer

    raise SyntaxError


def process_message(message: str) -> str:
    response_message = ''

    try:
        response_message = search_answer_by_message(message)

        for food in read_foods():
            if response_message == food:
                response_message = get_location_for_key(food)['name']
    except Exception as e:
        response_message = "Não entendi o que você disse..."

    return response_message

'''
texts = [
    [ 
        "Que delícia!\n",
        "Adoro este também\n",
        "Esse é o meu preferido, segredinho nosso hein\n",
    ],
    [
        "Deixa eu procurar aqui...\n",
        "Deixa eu dar uma olhadinha nos meus registros...\n",
        "Deixa eu ver...\n"
    ],
    [
        "Achei um local bem especial pra você\n",
        "Achei um local que você pode gostar, dá uma olhada\n",
        "Olha só esse local que eu achei pra você\n"
    ],
]
 
print("Olá ser humano! Sou Namaria, um bot feito exclusivamente para lhe ajudar a escolher um restaurante!")
user_name = input("Você poderia me informar seu nome meu anjo?\n")

key_word = input("Prazer {}, o que você geralmente come quando sai ?\n".format(user_name))

print(texts[0][random.randint(0,3)])

print(texts[1][random.randint(0,3)])

get_location_for_key(key_word)
'''

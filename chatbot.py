# Seguinte, a merda do Chatterbot precisava de muito treinamento pra não ficar soltando umas frases nada a ver no meio da conversa, então foda-se, vamo fazer na mão msm. 
# Mas rlx que é parada simples, A gente tem só que desenvolver um diálogo bacaninha aqui, a idéia é conseguir pegar uma palavra chave nas respostas do usuário
# por exemplo: hambúrguer, sanduíche, sushi, esse tipo de coisa, a partir dessa palavra chave a gente vai usar a API do Google Places pra ele indicar um local de Manaus e pronto.
# sintam-se a vontade pra desenvolver melhor isso daí, pq esse diálogo tá uma bosta

import random
from apicaller import get_location_for_key

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
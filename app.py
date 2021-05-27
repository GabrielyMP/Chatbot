from flask import Flask, jsonify, render_template, request

app = Flask(__name__, static_url_path='', static_folder='web/static', template_folder='web')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        json = request.get_json()

        request_message = json['content']

        print(request_message)

        # Chatbot vai processar a mensagem aqui

        response_message = 'Bla bla bla. Você fala demais, amigo!'

        return jsonify(content=response_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()

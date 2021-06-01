from flask import Flask, jsonify, render_template, request
#from flask_cors import CORS, cross_origin

import chatbot

app = Flask(__name__, static_url_path='', static_folder='web/static', template_folder='web')

#cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET', 'POST'])
#@cross_origin()
def index():
    if request.method == 'POST':
        json = request.get_json()

        request_message = json['content']

        # response_message = chatbot.process_message(request_message)

        request_message = ''

        return jsonify(content=response_message)

    return render_template('index.html')

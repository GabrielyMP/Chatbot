from flask import Flask, jsonify, render_template, request

app = Flask(__name__, static_url_path='', static_folder='web/static', template_folder='web')

@app.route('/message', methods = ['POST'])
def process_message():
    request_data = request.get_json()

    message = request_data['message']

    print(message)

    return jsonify(message=message)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

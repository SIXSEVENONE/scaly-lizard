from flask import Flask, render_template, request
from apidata.exceptions import VKApiException

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass

    return render_template(index.html)

@app.errorhandler(VKApiException)
def handle_api_error(error):
    return render_template('error.html', message=error)
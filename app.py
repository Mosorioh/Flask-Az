from flask import Flask
from flask import jsonify
import json
from flask import json

app = Flask(__name__)

@app.route('/test')
def test():
    return 'Pagina test API-REST con Env'

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, jsonify, request, make_response
from flask_restful import Api, Resource
from flask_cors import CORS
from random import *
# from isbn import RAKUTENAPI
# from sql import sql_arg
# RA = RAKUTENAPI()
# SQLARG = sql_arg()

# FlaskとVueの連携
app = Flask(__name__, static_folder='../../frontend/dist/static', template_folder='../../frontend/dist')
# 日本語
app.config['JSON_AS_ASCII'] = False
# CORS=Ajaxで安全に通信するための規約
api = Api(app)
CORS(app)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    print('index')
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

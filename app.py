import os

from flask import render_template, jsonify, Flask, request, send_from_directory
from flask_restful import Api,Resource,reqparse
from prime import prime

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@app.route('/', defaults={'path':''})
def home_page(path):
    return send_from_directory(app.static_folder,'index.html')


@app.route('/prime', methods=['POST'])
def check_prime():
    if request.method == 'POST':
        string = ''
        try:
            num = int(request.form['num'])
            flag = prime(num)
            if flag:
                string = str(num) + ' is a prime number'
            else:
                string = str(num) + ' is not a prime number'
        except ValueError:
            string = 'Please enter an integer'
        except TypeError:
            string = 'Please enter an integer greater than zero'
        finally:
            return render_template('form.html',results = string)


api.add_resource(HelloWorld,'/flask/hello')

if __name__ == '__main__':
    app.run(debug=True)

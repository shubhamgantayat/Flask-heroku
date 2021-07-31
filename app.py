from flask import render_template, jsonify, Flask, request, send_from_directory
from prime import prime
from flask_cors import cross_origin

app = Flask(__name__, static_url_path='', static_folder='frontend/build')


@app.route('/', defaults={'path':''})
@cross_origin()
def home_page(path):
    return send_from_directory(app.static_folder,'index.html')


@app.route('/prime', methods=['POST'])
@cross_origin()
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


if __name__ == '__main__':
    app.run(debug=True)

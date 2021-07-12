from flask import render_template, jsonify, Flask, request
from prime import prime

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home_page():
    return render_template('form.html')


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


if __name__ == '__main__':
    app.run(debug=True)

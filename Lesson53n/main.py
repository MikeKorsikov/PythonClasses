from random import randint

from flask import Flask, render_template, request, make_response
from forms import LoginForm
import os

# render_template()
app = Flask(__name__, template_folder='templates')  # , static_folder='static'
app.config['SECRET_KEY'] = os.urandom(12).hex()


class Person:
    def __init__(self, name, age, position=None):
        self.name = name
        self.age = age
        self.position = position


@app.route("/")
def index():
    user_list = [Person('alex <p> asd </p>  asd', 10.256),
                 Person('ron', 20, 'hr'),
                 Person('John', 15, 'dev'), Person('Ali', 30, 'cto')]
    return render_template('index.html', ls=user_list)


@app.route("/about.html")
def about():
    context = dict(name='Alex', age=10, position='dev')
    return render_template('about.html', **context)


@app.route("/login.html", methods=['post', 'get'])
def login():
    form = LoginForm()
    message = ''
    user_present = ''

    if request.cookies.get("login"):
        user_present = request.cookies.get("login")

    if request.method == 'POST':
        username = request.form['login']
        password = request.form.get('password')
        print(form.validate())
        print(form.errors)
        if username == 'admin' and password == 'pass':
            message = 'Data is correct'
        else:
            message = 'Wrong login'
        res = make_response(render_template('login.html',
                                            form=form,
                                            user_present=user_present,
                                            message=message))
        res.set_cookie('login', username, 60)
        return res

    return render_template('login.html', form=form, user_present=user_present)


# @app.route("/cookie.html")
# def cookie():
#     res = make_response(render_template('login.html'))
#     res.set_cookie('my', 'c', 60 * 4)
#     return res


@app.errorhandler(404)
def error_404(error):
    return 'errorhandler'


if __name__ == "__main__":
    app.run(debug=True)

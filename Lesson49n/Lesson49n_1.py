# 15/12/2022 Flask

from flask import Flask, request, make_response, redirect

app = Flask(__name__)


# Option-1 through decorator
@app.route("/")
def index_page():
    print("Launching page via option 1")
    res = make_response('<h1>Hello</h1>')
    res.headers['Content-type'] = 'text/html'
    res.headers['MyHeader'] = 'myHeaderData'
    res.set_cookie('c1', 'data1')
    return res
    # f"<h1>index page: IP {request.user_agent}, {request.remote_addr}</h1>"


@app.route("/error")
def error_page():
    return make_response('404 Error page', 400)


@app.route("/home")
def home_page():
    return "Home page"

@app.route("/hh")
def reroute():
    return redirect('http://127.0.0.1:5000/', code=302)

@app.route("/about1/")
@app.route("/about2/")
def about_page():
    return "About page"


@app.route("/user/<int:user_id>")
def user_page(user_id):
    print(type(user_id))
    return f"User {user_id}"


# Option-2 through function
# def index():
#     print("Launching page via option 2")
#     return "index page"
# app.add_url_rule('/', 'index', index)


if __name__ == "__main__":
    app.run(debug=True)

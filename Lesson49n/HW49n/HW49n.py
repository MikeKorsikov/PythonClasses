from flask import Flask, render_template

app = Flask(__name__, template_folder='HWtemplates')


@app.route("/")
def index():
    print('Home page...')
    return render_template('index.html')


@app.route("/main.html")
def main():
    print('Main page...')
    return render_template('main.html')


@app.route("/news.html")
def news():
    print('News page...')
    return render_template('news.html')


@app.route("/leadership.html")
def leadership():
    print('Leadership page...')
    return render_template('leadership.html')


@app.route("/about.html")
def about():
    print('About page...')
    return render_template('about.html')


@app.route("/contacts.html")
def contacts():
    print('Contacts page...')
    return render_template('contacts.html')


@app.errorhandler(404)
def error_404(error):
    return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=True)

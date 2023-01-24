# application 'phonebook' using flask

from flask import Flask, render_template, g, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import sqlite3
import os

app = Flask("Phonebook", template_folder="templates")
app.config['SECRET_KEY'] = os.urandom(12).hex()


class NewRecordForm(FlaskForm):
    name = StringField("Name")
    phone = StringField("Phone")
    submit = SubmitField("Submit")


@app.route("/")
def main():
    # todo menu with options
    # todo add display all contacts option
    # todo add add contact option
    # todo add search contact option
    # todo add delete contact option
    pass
    return render_template("main.html", title="Welcome")


@app.route("/all")
def show_all():
    # todo add query to DB
    # todo add display retrieved data [display()?]
    pass
    return render_template("all.html", title="All records")


@app.route("/new", methods=['GET', 'POST'])
def new_record():
    conn = get_db()
    c = conn.cursor()
    form = NewRecordForm()

    if request.method == 'POST':
        c.execute("""INSERT INTO contacts
                    (name, phone)
                    VALUES(?,?)""",
                  (
                      form.name.data,
                      form.phone.data
                  )
                  )
        conn.commit()
        flash("Record {} has been successfully submitted".format(request.form.get("name")), "success")
        return redirect(url_for("main"))
    return render_template("new.html", form=form)

    # todo use form
    # todo use class
    # todo save to DB [submit button]
    # todo display what was saved  [display()?]
    pass
    return render_template("new.html", title="New record")


@app.route("/edit", methods=['GET', 'POST'])
def edit_record():
    # todo add search record [use search_record()]
    # todo display found record [display()?]
    # todo add new details
    # todo save record to DB [submit button]
    # todo add exception if record not found
    pass
    return render_template("edit.html", title="Edit record")


@app.route("/search")
def search_record():
    # todo add search record by name etc
    # todo retrieve data from DB
    # todo display found details [display()?]
    # todo add error exception if no records found
    pass
    return render_template("search.html", title="Search record")


@app.route("/delete", methods=['GET', 'POST'])
def delete_record():
    # todo add search record [use search_record()]
    # todo display record found [display()?]
    # todo save to DB [submit button]
    pass
    return render_template("delete.html", title="Delete record")


@app.errorhandler(404)
def error(error):
    return render_template("error.html", title="Error")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('db/phonebook.db')
    return db


if __name__ == "__main__":
    app.run(debug=True)

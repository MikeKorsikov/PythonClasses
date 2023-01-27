# application 'phonebook' using flask

from flask import Flask, render_template, g, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Length
import sqlite3
import os

app = Flask("Phonebook", template_folder="templates")
app.config['SECRET_KEY'] = os.urandom(12).hex()


class RecordForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired("Input is required"),
                                           DataRequired("Data is required"),
                                           Length(min=5, max=20,
                                                  message="Input must be between 5 and 20 characters long")])
    phone = StringField("Phone", validators=[InputRequired("Input is required"),
                                             DataRequired("Data is required"),
                                             Length(min=6, max=15,
                                                    message="Input must be between 6 and 15 characters long")])


class NewRecordForm(RecordForm):
    submit = SubmitField("Submit")


class EditRecordForm(RecordForm):
    submit = SubmitField("Update record")


class DeleteRecordForm(RecordForm):
    submit = SubmitField("Delete record")


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
    conn = get_db()
    c = conn.cursor()
    records_from_db = c.execute("SELECT c.id, c.name, c.phone FROM contacts AS c")

    records = []
    for row in records_from_db:
        record = {
            "id": row[0],
            "name": row[1],
            "phone": row[2]
        }
        records.append(record)
    print(records)

    return render_template("all.html", title="All records", records=records)


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
    # todo display what was saved  [display()?]

    return render_template("new.html", title="New record")


@app.route("/record/<int:record_id>/edit", methods=['GET', 'POST'])
def edit_record(record_id):
    conn = get_db()
    c = conn.cursor()
    record_from_db = c.execute("SELECT * FROM contacts WHERE id = ?", (record_id,))
    row = c.fetchone()
    try:
        record = {
            "id": row[0],
            "name": row[1],
            "phone": row[2]
        }
    except:
        record = {}

    if record:
        form = EditRecordForm()
        if form.validate_on_submit():
            c.execute("UPDATE contacts SET name = ?, phone = ? WHERE id = ?",
                      (
                          form.name.data,
                          form.phone.data,
                          record_id
                      )
                      )
            conn.commit()

            flash("Record {} has been successfully updated".format(form.name.data), "success")
            return redirect(url_for("record", record_id=record_id))

        form.name.data = record["name"]
        form.phone.data = record["phone"]

        if form.errors:
            flash("{}".format(form.errors), "danger")
        return render_template("edit.html", record=record, form=form)
    return redirect(url_for("main"))


@app.route("/record/<int:record_id>")
def record(record_id):
    c = get_db().cursor()
    record_from_db = c.execute("""SELECT  c.id, c.name, c.phone 
    FROM contacts AS c WHERE c.id = ?""", (record_id,))
    row = c.fetchone()

    try:
        record = {
            "id": row[0],
            "name": row[1],
            "phone": row[2]
        }

    except:
        record = {}

    if record:
        deleteRecordForm = DeleteRecordForm()

        return render_template("record.html", record=record, deleteRecordForm=deleteRecordForm)
    return redirect(url_for("main"))


@app.route("/search")
def search_record():
    # todo add search record by name etc
    # todo retrieve data from DB
    # todo display found details [display()?]
    # todo add error exception if no records found
    pass
    return render_template("search.html", title="Search record")


@app.route("/record/<int:record_id>/delete", methods=["POST"])
def delete_record(record_id):
    conn = get_db()
    c = conn.cursor()

    record_from_db = c.execute("SELECT * FROM contacts WHERE id = ?", (record_id,))
    row = c.fetchone()
    try:
        record = {
            "id": row[0],
            "name": row[1]
        }
    except:
        record = {}

    if record:
        c.execute("DELETE FROM contacts WHERE id = ?", (record_id,))
        conn.commit()

        flash("Record {} has been successfully deleted.".format(record["name"]), "success")
    else:
        flash("This record does not exist.", "danger")

    return redirect(url_for("main"))


@app.errorhandler(404)
def error(error):
    return render_template("error.html", title="Error")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('db/phonebook.db')
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(debug=True)

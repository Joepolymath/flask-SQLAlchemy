from enum import unique
from flask import Flask, redirect
import os
from flask import render_template
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask import request
app = Flask(__name__)

# finding the current app path. (Location of this file)
project_dir = os.path.dirname(os.path.abspath(__file__))

# creating a database file (bookdatabase.db) in the above found path.
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

# connecting the database file (bookdatabase.db) to the sqlalchemy dependency.
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

# connecting this app.py file to the sqlalchemy
db = SQLAlchemy(app)

# @app.before_first_request
# def create_table():
#     db.create_all()

# creating a model for the book table in the diagram
class Book(db.Model):
    title = db.Column(db.String(80), unique = True, nullable = False, primary_key = True)
    # message = db.Column(db.String(80), unique = True, nullable = False)
    def __repr__(self):
        return "<Title: {}>".format(self.title)


@app.route('/')
def home():
    # validating the content of the form. This condition shall be false if the request.form list is empty
    books = Book.query.all() # this retrieves all the contents of the book table.
    return render_template('bookstore.html', iwe = books) # rendering the html page alongside the queried books to the browser.

@app.route('/sub', methods=["GET", "POST"])
def submitting():
    if request.form:
        twitter = request.form.get('ftitle') # assigns the content of the title field to the variable
        book = Book(title=twitter) # instance of the Book class. assigned to the 'book' variable
        db.session.add(book) # adds the data to the session
        db.session.commit() # this commits the data to the database
    return redirect(url_for('home'))
# @app.route('/bookstore')
# def bookstore():
#     return render_template('bookstore.html')

if __name__=="__main__":
    app.run(debug=True)

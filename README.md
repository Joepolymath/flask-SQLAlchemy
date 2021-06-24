# Study on SQLAlchemy

## Below are the steps to utilizing databases via the flask web frame work (as discussed in the Codeplateau class on 28th May, 2021):

### PLEASE NOTE: THIS NOTE ASSUMES THAT YOU ALREADY HAVE AT LEAST A VERY BASIC IDEA ON HOW TO BUILD A BASIC FLASK APP

1. In your virtual environment, install the following alongside your flask library; sqlalchemy, flask-sqlalchemy
The sqlalchemy is a dependency that connects the app to the sql database.
To import it;

        from flask_sqlalchemy import SQLAlchemy

2. Type in the following lines of codes;

(a) 

        project_dir = os.path.dirname(os.path.abspath(__file__))
This finds the current location of your python file (flask python app). It works on all Operating systems (os). It is worthy of note that you must import the os module before this works. 

        import os

(b) 

        database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))
This creates a database file (.db file) in the above found directory.
(c) 

        app.config["SQLALCHEMY_DATABASE_URI"] = database_file
Connects the database file to sqlalchemy.

(d) 

        db = SQLAlchemy(app)
Connects your .py file or app to the sqlalchemy

After these are done, you can hence proceed to step 3

3. Create a model for your book table. In this case, the table is only going to carry one column, which is "title".

4. Make sure the route in which the database will interact is set to the GET and POST methods.

        @app.route('/', methods=["GET", "POST"])
Also make sure that your form element on the html file has its method set to POST

        <form action="/" method="POST">
                <input type="text" name="title">
                <input type="submit" value="Add">
            </form>
5. To finally create the database, 
(a) go to your terminal and navigate to the virtual environment (if you haven't).
(b) enter the python shell by entering the 'python3' command
(c) type this -> 

        from app import db
please take note that 'app.py' is the name of my python file

6. Time to request from the form
To use the request module, you will have to import it
from flask import request

After being imported, it is worthy of note that the the request.form property returns a dictionary if the submit button is clicked. This dictionary is empty if the submit button isn't clicked yet.
The contents of the dictionary are the contents of the form. The data on the form gets parsed into the dictionary.

PLEASE CHECK THE app.py FILE TO SEE THE REMAINING STEPS AS COMMENTS.

TAKE NOTE OF THY SYNTAXES. 

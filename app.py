from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def homepage():
    """Home page displays a list of pets."""

    pets = Pet.query.all()

    return render_template("homepage.html", pets=pets)

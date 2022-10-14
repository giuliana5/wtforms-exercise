from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, Pet, db
from forms import AddPetForm

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

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Creates form to add a pet..."""

    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")
    else:
        return render_template("add-pet.html", form=form)

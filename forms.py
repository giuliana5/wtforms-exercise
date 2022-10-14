from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange

class AddPetForm(FlaskForm):
    """Form to add a new pet."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=["Cat", "Dog", "Porcupine"])
    photo_url = URLField("Image URL")
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Invalid Age")])
    notes = StringField("Notes")

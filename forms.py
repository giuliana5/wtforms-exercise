from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange

class AddPetForm(FlaskForm):
    """Form to add a new pet."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=["Cat", "Dog", "Porcupine"])
    photo_url = URLField("Image URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Invalid Age")])
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form to edit existing pet."""

    photo_url = URLField("Image URL", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available")
    
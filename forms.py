from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    """Form to add a new pet."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = URLField("Image URL")
    age = IntegerField("Age", validators=[Optional()])
    notes = StringField("Notes")

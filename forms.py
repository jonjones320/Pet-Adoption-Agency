"""Forms for the Pet Adoption Agency."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField("Name", 
                       validators=[InputRequired(message="Please name your pet")])
    species = SelectField("Species", 
                          choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Porcupine', 'Porcupine')], 
                          validators=[InputRequired(message="Please make a selection")])
    photo_url = StringField("Pet Pic", 
                            validators=[Optional(), URL(require_tld=False, 
                            message="Please provide a valid photo URL")])
    age = FloatField("Age", validators=
                                [Optional(), 
                                NumberRange(min=0, max=50, message="Age must be within 0-50")])
    notes = StringField("Notes", 
                        validators=[Optional()])
    available = BooleanField("This pet is available for adoption", default=True)

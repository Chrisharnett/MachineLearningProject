import decimal

from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields import SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired


class VehicleInformationForm(FlaskForm):
    carCylinders = IntegerField("Cylinders:", validators=[DataRequired()])
    carHorsepower = DecimalField("Horsepower:", places=2, rounding=decimal.ROUND_UP, validators=[DataRequired()])
    carWeight = IntegerField("Weight:", validators=[DataRequired()])
    carYear = IntegerField("Year:", validators=[DataRequired()])
    carOrigin = SelectField("Origin:", choices=["USA", "Japan", "Europe"], validators=[DataRequired()])

    submit = SubmitField("Submit")

class PersonalDataForm(FlaskForm):
    personAge = IntegerField("Age:", validators=[DataRequired()])
    personBMI = DecimalField("BMI:", places=2, rounding=decimal.ROUND_UP, validators=[DataRequired()])
    personGlucose = IntegerField("Glucose:", validators=[DataRequired()])

    submit = SubmitField("Submit")
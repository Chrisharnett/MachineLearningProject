import decimal

from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields import SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, NumberRange


class VehicleInformationForm(FlaskForm):
    carCylinders = IntegerField("Cylinders:", validators=[DataRequired(), NumberRange(min=3, max=12)])
    carHorsepower = DecimalField("Horsepower:", places=2, rounding=decimal.ROUND_UP, validators=[DataRequired(), NumberRange(min=40, max=200)])
    carWeight = IntegerField("Weight:", validators=[DataRequired(), NumberRange(min=1500, max=5200)])
    carYear = IntegerField("Year:", validators=[DataRequired(), NumberRange(min=1950, max=2024)])
    carOrigin = SelectField("Origin:", choices=["USA", "Japan", "Europe"], validators=[DataRequired()])

    submit = SubmitField("Submit")

class PersonalDataForm(FlaskForm):
    personAge = IntegerField("Age:", validators=[DataRequired(), NumberRange(min=1, max=120)])
    personBMI = DecimalField("BMI:", places=2, rounding=decimal.ROUND_UP, validators=[DataRequired(), NumberRange(min=1, max=70)])
    personGlucose = IntegerField("Glucose:", validators=[DataRequired(), NumberRange(min=1, max=200)])

    submit = SubmitField("Submit")
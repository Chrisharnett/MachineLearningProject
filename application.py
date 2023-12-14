from flask import Flask, render_template
from forms import VehicleInformationForm, PersonalDataForm
from datetime import datetime
from machines import lpkPrediction, diabetesPrediction
import os
import warnings

warnings.filterwarnings("ignore")

application = Flask(__name__)
# This is a comment
application.config['SECRET_KEY'] = 'nvmnkfwslzmnx.kj456/W?ERIU&WE(F*&/hksef;g98734:SP(&D'
application.config['SUBMITTED_DATA'] = os.path.join('static', 'data', '')
application.config['SUBMITTED_IMG'] = os.path.join('static', 'img', '')

@application.route('/', methods=['POST', 'GET'])
def welcome():
    return render_template('index.html')

@application.route('/diabetesMachine', methods=['POST', 'GET'])
def diabetesMachine():
    form = PersonalDataForm()
    if form.validate_on_submit():

        person_age = form.personAge.data
        person_bmi = form.personBMI.data
        person_glucose = form.personGlucose.data

        prediction = diabetesPrediction({"age": person_age, "bmi": person_bmi, "glucose": person_glucose})
        if prediction == 0:
            return render_template("diabetesMachine.html", form=form, result="False")
        else:
            return render_template("diabetesMachine.html", form=form, result="True")

    else:
        return render_template('diabetesMachine.html', form=form)


@application.route('/kplMachine', methods=['POST', 'GET'])
def lpkMachine():
    form = VehicleInformationForm()
    if form.validate_on_submit():
        cyl = form.carCylinders.data
        horsepower = form.carHorsepower.data
        weight = form.carWeight.data
        year = form.carYear.data
        origin = form.carOrigin.data

        if origin == "USA":
            vehicle = {"cylinders": cyl, "horsepower": horsepower, "weight": weight,
                        "age": datetime.today().year - year, "origin_japan": 0, "origin_usa": 1}
        elif origin == "Japan":
            vehicle = {"cylinders": cyl, "horsepower": horsepower, "weight": weight,
                        "age": datetime.today().year - year, "origin_japan": 1, "origin_usa": 0}
        else:
            vehicle = {"cylinders": cyl, "horsepower": horsepower, "weight": weight,
                        "age": datetime.today().year - year, "origin_japan": 0, "origin_usa": 0}

        result = lpkPrediction(vehicle)

        return render_template("lpkMachine.html", form=form, result = round(result, 0))

    else:
        return render_template('lpkMachine.html', form=form)


if __name__ == '__main__':
    application.run()

from flask import Flask, render_template
from forms import VehicleInformationForm, PersonalDataForm
from datetime import datetime
import os
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

app.config['SECRET_KEY'] = 'nvmnkfwslzmnx.kj456/W?ERIU&WE(F*&/hksef;g98734:SP(&D'
app.config['SUBMITTED_DATA'] = os.path.join('static', 'data', '')
app.config['SUBMITTED_IMG'] = os.path.join('static', 'img', '')

@app.route('/', methods=['POST', 'GET'])
def welcome():
    return render_template('index.html')

@app.route('/diabetesMachine', methods=['POST', 'GET'])
def diabetesMachine():
    form = PersonalDataForm()
    if form.validate_on_submit():

        person_age = form.personAge.data
        person_bmi = form.personBMI.data
        person_glucose = form.personGlucose.data

        person_dict = {"age": person_age, "bmi": person_bmi, "glucose": person_glucose}

        return render_template("viewDiabeticResults.html", person_dict=person_dict)

    else:
        return render_template('diabetesMachine.html', form=form)


@app.route('/kplMachine', methods=['POST', 'GET'])
def kplMachine():
    form = VehicleInformationForm()
    if form.validate_on_submit():
        car_cylinders = form.carCylinders.data
        car_hp = form.carHorsepower.data
        car_weight = form.carWeight.data
        car_year = form.carYear.data
        car_origin = form.carOrigin.data

        if car_origin == "USA":
            car_dict = {"cylinders": car_cylinders, "horsepower": car_hp, "weight": car_weight,
                        "age": datetime.today().year - car_year, "origin_japan": 0, "origin_usa": 1}
        elif car_origin == "Japan":
            car_dict = {"cylinders": car_cylinders, "horsepower": car_hp, "weight": car_weight,
                        "age": datetime.today().year - car_year, "origin_japan": 1, "origin_usa": 0}
        else:
            car_dict = {"cylinders": car_cylinders, "horsepower": car_hp, "weight": car_weight,
                        "age": datetime.today().year - car_year, "origin_japan": 0, "origin_usa": 0}

        return render_template("viewMPGResults.html", car_dict=car_dict)

    else:
        return render_template('kplMachine.html', form=form)


@app.route('/vehicleInformation', methods=['POST', 'GET'])
def get_vehicle_information():
    form = VehicleInformationForm()
    if form.validate_on_submit():
        car_cylinders = form.carCylinders.data
        car_hp = form.carHorsepower.data
        car_weight = form.carWeight.data
        car_year = form.carYear.data
        car_origin = form.carOrigin.data

        if car_origin == "USA":
            car_dict = {"cylinders": car_cylinders, "horsepower": car_hp, "weight": car_weight,
                        "age": datetime.today().year - car_year, "origin_japan": 0, "origin_usa": 1}
        elif car_origin == "Japan":
            car_dict = {"cylinders": car_cylinders, "horsepower": car_hp, "weight": car_weight,
                        "age": datetime.today().year - car_year, "origin_japan": 1, "origin_usa": 0}
        else:
            car_dict = {"cylinders": car_cylinders, "horsepower": car_hp, "weight": car_weight,
                        "age": datetime.today().year - car_year, "origin_japan": 0, "origin_usa": 0}

        return render_template("viewMPGResults.html", car_dict=car_dict)

    else:
        return render_template("vehicleInfo.html", form=form)

if __name__ == '__main__':
    app.run()

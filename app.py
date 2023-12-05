from flask import Flask, redirect, url_for, render_template, flash
import os

application = Flask(__name__)

application.config['SECRET_KEY'] = 'nvmnkfwslzmnx.kj456/W?ERIU&WE(F*&/hksef;g98734:SP(&D'
application.config['SUBMITTED_DATA'] = os.path.join('static', 'data', '')
application.config['SUBMITTED_IMG'] = os.path.join('static', 'img', '')

@application.route('/', methods=['POST', 'GET'])
def welcome():
    return render_template('index.html')

@application.route('/diabetesMachine', methods=['POST', 'GET'])
def diabetesMachine():
    """
    Form for users to enter data.
    """
    return render_template('diabetesMachine.html')

@application.route('/kplMachine', methods=['POST', 'GET'])
def kplMachine():
    """
    Form for users to enter data.
    """
    return render_template('kplMachine.html')

if __name__ == '__main__':
    application.run()

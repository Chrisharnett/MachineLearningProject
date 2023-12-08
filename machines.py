from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from joblib import load

def lpkPrediction(vehicle):
    model = load('machines/mpg_model.joblib')

    mpg = model.predict([[
        float(vehicle.get('cylinders')),
        float(vehicle.get('horsepower')),
        float(vehicle.get('weight')),
        float(vehicle.get('age')),
        vehicle.get('origin_japan'),
        vehicle.get('origin_usa')]])
    # Convert miles per gallon to litres per 100 kilometers.
    if mpg is not None and mpg[0] > 0:
        return 235.21/mpg[0]
    else:
        return

def diabetesPrediction(humanStats):
    model = LogisticRegression()
    model = load('machines/diabetes_prediction.joblib')
    outcome = model.predict([[
        float(humanStats.get('age')),
        float(humanStats.get('bmi')),
        float(humanStats.get('glucose')),
    ]])
    if outcome == True:
        return True
    return False

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from joblib import load

def lpkPrediction(vehicle):
    model = LinearRegression()
    model = load('machines/mpg_model.joblib')

    mpg = model.predict([[
        float(vehicle.get('cylinders')),
        float(vehicle.get('horsepower')),
        float(vehicle.get('weight')),
        float(vehicle.get('age')),
        float(vehicle.get('origin_japan')),
        float(vehicle.get('origin_usa'))]])
    # Convert miles per gallon to litres per 100 kilometers.
    if mpg:
        return 235.21/mpg
    else:
        return

def diabetesPrediction(humanStats):
    model = LogisticRegression()
    model = load('/machines/diabetes_prediction')
    return model.predict(humanStats)

from flask import Flask, jsonify, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("iris_logistic_regression.pkl", "rb"))


@app.route("/")
def hello():
    return "Welcome to the Iris Classification API"


@app.route("/predict", methods=["POST"])
def predict():

    input_data = request.json
    values = [list(input_data.values())]

    labels = {
        0: "Iris Setosa",
        1: "Iris Versicolour",
        2: "Iris Virginica"
    }

    probabilities = model.predict_proba(values)[0]
    prediction = labels[probabilities.argmax()]
    confidence = round(probabilities.max()*100, 2)

    return jsonify({'prediction': prediction, "confidence": confidence})


app.run(debug=True)

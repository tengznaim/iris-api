from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/predict")
def predict():
    return "This is where the prediction would go"


app.run(debug=True)

from flask import Flask, render_template, request, url_for
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def predict_from_api():

    if request.method == "POST":
        body = {
            "sepal_width": None,
            "sepal_length": None,
            "petal_length": None,
            "petal_width": None,
        }

        body["sepal_width"] = float(request.form["sepal_width"])
        body["sepal_length"] = float(request.form["sepal_length"])
        body["petal_length"] = float(request.form["petal_length"])
        body["petal_width"] = float(request.form["petal_width"])

        response = requests.post("http://127.0.0.1:5000/predict", json=body)

        return render_template("predict.html", prediction=response.json())

    return render_template("index.html")


app.run(port=5001, debug=True)

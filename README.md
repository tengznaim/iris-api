# Iris Classification API with Flask

This is a sequel to a previous project on training a logistic regression model to classify Iris species. [https://github.com/tengznaim/iris-classification]. In this repository, the trained model is then used to make a simple API with a prediction endpoint using Flask. It also includes a simple web application also built using Flask to complement the API.

![image](https://user-images.githubusercontent.com/63803360/131960289-b9d6130d-e164-41b4-88ec-def3102f1433.png)

![image](https://user-images.githubusercontent.com/63803360/131960313-9c6f7d57-9472-4d62-8171-cc04bc3a9d41.png)

By using Flask, it's technically possible to render pages immediately from the same script but I wanted to practice creating an endpoint that can be called from another web application, even though that application is also built using Flask.

## The API `iris-api.py`

This is a simple API built using Flask. The script loads a trained model that was serialized using pickle and has a "/predict" endpoint that makes and returns a prediction based on one set of input.

## The Web App `app.py`

This is a web application built using Flask that renders an input page to get input for the model and later displays the result of the prediction.

## Current Limitations

- The endpoint only accepts one set of input and doesn't support things like batch predictions.
- The web app is not mobile responsive because at the time of writing, I just haven't designed it to be.
- Current styling is spaghetti code and due for refactoring.

## Running This Locally

1. Open two terminals.
2. Run the API using `py iris-api.py` on one terminal.
3. Run the web app using `py app.py` on the other terminal.
   - Note that the API is configured to run on port 5000 and the web app on 5001. Feel free to change this in the respective files.
4. Go to 127.0.0.1:5001 to play around with the web app.

## References

1. Turning Models to APIs

   - https://www.datacamp.com/community/tutorials/machine-learning-models-api-python

2. Styling Range Inputs
   - https://www.youtube.com/watch?v=Ow0QjqmaRtQ
   - https://www.youtube.com/watch?v=3Eb6FtjkZ_k

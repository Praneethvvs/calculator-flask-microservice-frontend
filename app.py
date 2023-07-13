import requests
from flask import Flask, request, render_template
import os


backend_url = os.getenv("APP_URL")

# Create the app object
app = Flask(__name__)


# importing function for calculations

# Define calculator
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    a = request.form['a']
    b = request.form['b']
    operation = str(request.form['operation'])

    payload = {"operator1": a, "operator2": b, "operation": operation}

    # azure_internal_url = "https://container-app-backend.internal.blackcliff-8ab02ec6.eastus.azurecontainerapps.io"
    result_from_backend = requests.post(url=backend_url, json=payload)

    if result_from_backend.status_code == 200:
        result = result_from_backend.json()
        return render_template('index.html', prediction_text=str(result["result"]))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

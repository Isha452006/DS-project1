from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("sales_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            tv = float(request.form["TV"])
            radio = float(request.form["Radio"])
            newspaper = float(request.form["Newspaper"])
            new_data = np.array([[tv, radio, newspaper]])
            prediction = model.predict(new_data)[0]
        except:
            prediction = None  # If invalid input, set prediction to None
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
   app.run(debug=True, host='127.0.0.1', port=5001)


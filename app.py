from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Your form is here

@app.route('/predict', methods=['POST'])
def predict():
    # Get form values
    TV = float(request.form['TV'])
    Radio = float(request.form['Radio'])
    Newspaper = float(request.form['Newspaper'])

    # Dummy prediction (replace with your model logic)
    predicted_sales = TV * 0.04 + Radio * 0.3 + Newspaper * 0.02

    # Pass the prediction back to the template
    return render_template('index.html', prediction=round(predicted_sales, 2))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import pandas as pd
import pickle

model = pickle.load(open('iris_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():

    return render_template("index.html")

@app.route('/submit', methods =['POST'])
def predict():
    input_dict = {
        "sepal_length" : float(request.form['sl']),
        "sepal_width" : float(request.form['sw']),
        "petal_length" : float(request.form['pl']),
        "petal_width" : float(request.form['pw'])
    }

    input_df  = pd.DataFrame([input_dict])
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)

    if prediction == 0:
        result = "Your 🌸 is Setosa"
    elif prediction == 1:
        result = "Your 🌸 is Versicolour"
    elif prediction ==2:
        result = "Your 🌸 is Virginica"
    else:
        result = "UnKnown Species 🤷"



    return render_template('index.html', Result = result)


if __name__ == '__main__':
    app.run(debug=True)
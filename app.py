from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = [
        float(request.form['age']),
        float(request.form['height']),
        float(request.form['weight']),
        float(request.form['bmi']),
        float(request.form['ap_hi']),
        float(request.form['ap_lo']),
        int(request.form['cholesterol']),
        int(request.form['gluc']),
        int(request.form['smoke']),
        int(request.form['alco']),
        int(request.form['active'])
    ]

    prediction = model.predict([data])[0]
    result = "Disease Detected" if prediction == 1 else "No Disease"

    return render_template("index.html", prediction=result, form_data=request.form)

if __name__ == "__main__":
    app.run()

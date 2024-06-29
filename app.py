from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle


app = Flask(__name__)

model = pickle.load(open("best_model.pkl", "rb"))
df = pd.read_csv('data.csv')


@app.route('/')
def index():
    Gender = sorted(df['Gender'].unique())
    return render_template('index.html', Gender=Gender)


@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form.get('Age'))
    # gender = int(request.form.get('Gender'))
    total_bilirubin = float(request.form.get('Total_Bilirubin'))
    direct_bilirubin = float(request.form.get('Direct_Bilirubin'))
    Alkaline_Phosphotase = float(request.form.get('Alkaline_Phosphotase'))
    Alamine_Aminotransferase = float(request.form.get('Alamine_Aminotransferase'))
    Aspartate_Aminotransferase = float(request.form.get('Aspartate_Aminotransferase'))
    Total_Protiens = float(request.form.get('Total_Protiens'))
    Albumin = float(request.form.get('Albumin'))
    Albumin_and_GlobulinRatio = float(request.form.get('Albumin_and_Globulin_Ratio'))

    print(age, total_bilirubin, direct_bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_GlobulinRatio)

    prediction = model.predict(pd.DataFrame([[age, total_bilirubin, direct_bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_GlobulinRatio]],
    columns=['Age', 'Total Bilirubin', 'Direct Bilirubin', 'Alkaline Phosphotase', 'Alamine Aminotransferase', 'Aspartate Aminotransferase', 'Total Protiens', 'Albumin', 'Albumin_and_Globulin_Ratio']))
    prediction = int(prediction)
    print(prediction)
    return jsonify(prediction)
    

 
if __name__ == "__main__":
    app.run()
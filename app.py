#import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('Model_wo_DPF.pkl', 'rb'))

# default page of our web-app


@app.route('/')
def home():
    return render_template('index.html')

# To use the predict button in our web-app


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict_proba(final_features)[:, 1]

    output = float(prediction)

    prediction_text = f'Your chances of having diabetes are {output*100}%.\n'

    if (output >= 0.85):
        prediction_text = prediction_text + 'You should consider seeing a doctor.'
    elif(output >= 0.45):
        prediction_text = prediction_text + 'You are likely to develop Diabetes.'
    else:
        prediction_text = prediction_text + 'Congratulations!!!! You are healthy.'

    return render_template('prediction.html', prediction_text=prediction_text)


@app.route('/bmichart', methods=['POST'])
def bmichart():
    '''
    Displays BMI Chart
    '''
    # bmiParam[0]= weight
    bmiParam = [float(x) for x in request.form.values()]
    bmiResult = float(bmiParam[0])/(float(bmiParam[1])**2)

    output = str(round(bmiResult, 2))
    return render_template('bmiChart.html', BMI_cal='Your BMI is : {}'.format(output))


@app.route('/INDEX')
def INDEX():
    '''
    For GOING TO HOME PAGE
    '''
    return render_template('index.html')


@app.route('/BMI')
def BMI():
    '''
    For GONG TO BMI PAGE
    '''
    return render_template('BMI.html')


@app.route('/DIABETES')
def DIABETES():
    '''
    For GOING TO TIPS PAGE
    '''
    return render_template('diabetes.html')


@app.route('/FOOD')
def FOOD():
    '''
    For GOING TO FOOD PAGE
    '''
    return render_template('food.html')


@app.route('/MEDICINE')
def MEDICINE():
    '''
    For GOING TO MEDICINE PAGE
    '''
    return render_template('medicine.html')


@app.route('/PREDICTION')
def PREDICTION():
    '''
    For GOING TO PREDICTION PAGE
    '''
    return render_template('prediction.html')


if __name__ == "__main__":
    app.run(debug=True)

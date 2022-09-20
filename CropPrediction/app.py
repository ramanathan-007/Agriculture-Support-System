#!/usr/bin/env python
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
main = pickle.load(open('main.pkl','rb'))

@app.route('/')
def home():
    return  render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = main.predict(final_features)

    output = prediction[0]

    return render_template('index.html', prediction_text='The Crop suitable for the given climatic condition is {} .'.format(output))

@app.route('/predict_api',methods=['post'])
def predict_api():

      data= request.get_json(force=True)
      prediction = main.predict([np.array(list(data.values()))])

      output = prediction[0]
      return jsonify(output)

if __name__== "__main__":
    app.run(debug=True)
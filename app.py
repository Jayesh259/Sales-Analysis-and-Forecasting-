# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

import numpy as np
##import tensorflow as tf
##from tensorflow import keras
import pandas as pd
import requests
import pickle 

import sklearn

  

app = Flask(__name__)

file = open('model.pkl','rb')

m1 = pickle.load(file) 

##model2 = pickle.load(open('LGBM.pkl','rb'))
##model3 = keras.models.load_model("DNN_MODEL")
## model4 = keras.models.load_model("MLP_MODEL")

@app.route('/',methods = ['GET'])
def Home():
    return render_template('main.html')

@app.route("/index",methods = ['POST','GET'])
def forecast():
    return render_template('index.html')

@app.route("/analysis",methods = ['POST','GET'])
def analysis():
    return render_template('analysis.html')

 

@app.route("/predict",methods=['POST'])
def predict():
  
    if request.method == 'POST':
        P = int(request.form['Product'])
        
            
        
        S =  int(request.form['Store'])
        
        
        X=pd.read_csv('X.csv')
        X['item']=P
        X['store']=S
        X.drop(columns='date',inplace=True)
        ##if a == 1:
          #  X = np.asarray(X).astype(np.float32)  
            
        prediction = m1.predict(X)
        A = [int(a) for a in prediction]
        s=sum(A)
        avg = int(s/len(A))
        A = [str(a) for a in A]
        j=[]
        for i in range(1,32):
            j.append(i)
        j = [str(i) for i in j]
        j = ['Day '+i for i in j]
        res = {}
        res = dict(zip(j, A))
        
       ## return redirect(url_for("index"), res = res , prediction_text2 = 'Total Sales Forecast for next month : {}'.format(s) , prediction_text3 = 'Average Sale per Day: {} '.format(avg))
      
    return render_template('index.html',prediction_text1= res , prediction_text2 = 'Total Sales Forecast for next month : {}'.format(s) , prediction_text3 = 'Average Sale per Day: {} '.format(avg))
   
            
if __name__=='__main__':
    app.run(debug=True)
            
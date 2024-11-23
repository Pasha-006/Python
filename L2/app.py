import pickle
import numpy as np
import pandas as pd
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def welcomePage():
    if request.method=="POST":
        age=request.form["Age"]
        gender=request.form['gender']
        education=request.form['education']
        income=request.form['Income']
        experience=request.form['Experience']
        home_ownership=request.form['House_ownership']
        loan_amount=request.form['Amount']
        interest_rate=request.form['InterestRate']
        percentageIncome=request.form['PercentageIncome']
        credHist=request.form['CredHist']
        CreditScore=request.form['CreditScore']
        loan_intent=request.form['Loan_intent']
        prevFile=request.form['PrevFile']
       
        #LabelEncoders=pickle.load('labelencoders.pkl')
        #gender=LabelEncoders[0].transform(gender) 
        probability=0
        with open('/home/shaikr4/Desktop/my_folder/ML/Regressions/Logistic_regression/labelencoders.pkl','rb') as file:
             model= pickle.load(file) 
             gender=model[0].transform([gender]) 
             education=model[1].transform([education])
             home_ownership=model[2].transform([home_ownership])
             loan_intent=model[3].transform([loan_intent])
             prevFile=model[4].transform([prevFile])
        with open('/home/shaikr4/Desktop/my_folder/ML/Regressions/Logistic_regression/Loan_predictor.pkl','rb') as file:
             model= pickle.load(file) 
             #new_data=pd.DataFrame([age,[[gender]],[[education]],[[income]],[[experience]],[[home_ownership]],[[loan_amount]],[[interest_rate]],[[percentageIncome]],[[credHist]],[[CreditScore]],[[loan_intent]],[[prevFile]]])
             probability=model.best_estimator_.predict_proba([[age,gender,education,income,experience,home_ownership,loan_amount,interest_rate,percentageIncome,credHist,CreditScore,loan_intent,prevFile]])

        print(probability)
        return str(0)

    return render_template("index.html")

if __name__=='__main__': 
    app.run(debug=True)


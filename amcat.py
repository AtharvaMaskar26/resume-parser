import streamlit as st

import numpy as np
import pandas as pd
import joblib

def show_amcat_page():
    prediction = 0

    def predict(): 
        global prediction
        columns = ['Quants', 'LogicalReasoning', 'Verbal', 'Programming', 'CGPA',
        'Networking', 'CloudComp', 'WebServices', 'DataAnalytics',
        'QualityAssurance', 'AI']

        row = np.array([quant, logicalReasoning, verbal, programming ,cgpa, networking, cloudComp, webServices, dataAnalytics, qualityAssuarance, ai]) 
        X = pd.DataFrame([row], columns = columns)
        prediction = model.predict(X)

        st.write(prediction)

        if (prediction == 0):
            st.write("Your chances for getting placed are less")
        else:
            st.write("Your scores for getting placed are good")


    model = joblib.load('xgb.joblib')
    st.title('Predict the salaries')
    st.header(prediction)
    # PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
    quant = st.number_input("Enter your quants grade", 5)
    logicalReasoning = st.number_input("Enter your logical reasoning grade", 5)
    verbal = st.number_input("Enter your verbal grade", 5)
    programming = st.number_input("Enter your programing grade", 5)
    cgpa = st.number_input("Enter your cgpa", 5)
    networking = st.number_input("Enter your networking grade", 5)
    cloudComp = st.number_input("Enter your Cloud Computing grade", 5)
    qualityAssuarance = st.number_input("Enter your QA grade", 5)
    webServices = st.number_input("Enter your web services grade", 5)
    dataAnalytics = st.number_input("Enter your Data Analytics grade", 5)
    ai = st.number_input("Enter your ai grade", 5)

    st.write(prediction)


    trigger = st.button('Predict', on_click=predict)

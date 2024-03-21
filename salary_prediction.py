import streamlit as st

import numpy as np
import pandas as pd
import joblib

def show_salary_prediction():
    prediction = 0

    def predict(): 
        global prediction
        columns = ['Gender', 'Degree', 'Specialization', 'CollegeState', 'collegeGPA',
            'CollegeCityTier', 'GraduationYear', '10percentage', '12graduation',
            '12percentage', 'CollegeTier']

        row = np.array([sex, degree_box, specialization_box, college_state, college_cgpa, city_tier, graduation_year, percentage_10, graduation_12, percentage_12, college_tier]) 
        X = pd.DataFrame([row], columns = columns)
        prediction = model.predict(X)

        st.write("You can earn a salary upto", prediction)


# Gender,Degree,Specialization,CollegeState,collegeGPA,CollegeCityTier,GraduationYear,10percentage,12graduation,12percentage,CollegeTier,Salary
    degrees = ['B.Tech/B.E.', 'M.Tech./M.E.', 'MCA', 'M.Sc. (Tech.)']
    gender = ['M', 'F']
    specialization = ['instrumentation and control engineering',
       'computer science & engineering',
       'electronics & telecommunications', 'biotechnology',
       'mechanical engineering', 'information technology',
       'electronics and communication engineering',
       'computer engineering', 'computer application',
       'computer science and technology', 'electrical engineering',
       'automobile/automotive engineering',
       'electronics and electrical engineering',
       'information science engineering', 'chemical engineering',
       'instrumentation engineering', 'electronics & instrumentation eng',
       'ceramic engineering', 'metallurgical engineering',
       'aeronautical engineering', 'electronics engineering',
       'electronics and instrumentation engineering',
       'applied electronics and instrumentation', 'civil engineering',
       'computer and communication engineering',
       'industrial & production engineering', 'computer networking',
       'other', 'electronics and computer engineering',
       'control and instrumentation engineering',
       'mechanical & production engineering', 'mechanical and automation',
       'industrial & management engineering', 'biomedical engineering',
       'electrical and power engineering',
       'telecommunication engineering', 'industrial engineering',
       'mechatronics', 'embedded systems technology', 'electronics',
       'information & communication technology', 'information science']

    states = ['Delhi', 'Uttar Pradesh', 'Maharashtra', 'Tamil Nadu', 'Punjab',
       'West Bengal', 'Telangana', 'Andhra Pradesh', 'Haryana',
       'Karnataka', 'Orissa', 'Chhattisgarh', 'Rajasthan',
       'Madhya Pradesh', 'Uttarakhand', 'Gujarat', 'Jharkhand',
       'Himachal Pradesh', 'Bihar', 'Union Territory',
       'Jammu and Kashmir', 'Kerala', 'Assam', 'Sikkim', 'Meghalaya',
       'Goa']


    model = joblib.load('xgbpipe.joblib')
    st.title('Predict the salaries')
    st.header(prediction)
# PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
    sex = st.selectbox("Enter your gender", gender)
    degree_box = st.selectbox("Select your degree: ", degrees)
    specialization_box = st.selectbox("Select your specialization: ", specialization)
    college_state = st.selectbox("Select your state: ", states)
    college_cgpa = st.number_input("Enter your college CGPA: ")
    city_tier = st.number_input("Enter your college city tier: ")
    graduation_year = st.number_input("Enter your graduation year: ")
    percentage_10 = st.number_input("Enter your 10th Percentage: ")
    graduation_12 = st.number_input("Enter your 12th graduation year: ")
    percentage_12 = st.number_input("Enter your 12th precentage: ")
    college_tier = st.number_input("Enter your college tier: ")
    st.write(prediction)





    

    trigger = st.button('Predict', on_click=predict)

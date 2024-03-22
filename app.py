import streamlit as st

from resume_analyzer import show_resume_analyzer_page
from salary_prediction import show_salary_prediction
from amcat import show_amcat_page

# show_resume_analyzer_page()
# show_salary_prediction()
# show_amcat_page()

page_names_to_funcs = {
    # "—": intro
    "Resume Analyzer": show_resume_analyzer_page,
    "Salary Predictor": show_salary_prediction,
    "amcat prediction": show_amcat_page,
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
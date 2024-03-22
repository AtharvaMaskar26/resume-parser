from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai


def show_resume_analyzer_page():
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    def get_gemini_response(input,pdf_cotent,prompt):
        model=genai.GenerativeModel('gemini-pro-vision')
        response=model.generate_content([input,pdf_content[0],prompt])
        return response.text

    def input_pdf_setup(uploaded_file):
        if uploaded_file is not None:
            ## Convert the PDF to image
            images=pdf2image.convert_from_bytes(uploaded_file.read())

            first_page=images[0]

            # Convert to bytes
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
                }
            ]
            return pdf_parts
        else:
            raise FileNotFoundError("No file uploaded")

## Streamlit App


    # st.set_page_config(page_title="ATS Resume EXpert")
    st.header("ATS Tracking System")
    input_text=st.text_area("Job Description: ",key="input")
    uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


    if uploaded_file is not None:
        st.write("PDF Uploaded Successfully")


    submit1 = st.button("Tell Me About the Resume")
    submit2 = st.button("Chances of getting placed")

#submit2 = st.button("How Can I Improvise my Skills")

    submit3 = st.button("Percentage match")
    submit4 = st.text_input("Enter any further questions you might have: ")

    input_prompt1 = """
        You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
        Please share your professional evaluation on whether the candidate's profile aligns with the role. 
         Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements. 
        """
    
    input_prompt2 = """
        You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
        your task is to evaluate the resume against the provided job description. Along with an ATS you are also a good HR who gives feedback. You have to give what are the chances of the candidate getting placed in the company in percentage. Also check for any grammer mistakes in the RESUME not in the question/prompt and mention them after the percentage of getting placed. At the end always give course suggestions on what courses should the candidate take to improve his resume, give it with proper course names scrapwed from the web, give it in bullet points. If the candidate has good chances print first line as chances of getting placed: and give a number between 50 and 100. If the candidate does not have good chances give a number between 25 to 50
        """
    
    

    input_prompt3 = """
    You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
    your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
    the job description. Give keyword Optimisation tips to improve visibility of the resume in ATS
 and prevent it from getting rejected, explain it in detail that would help the candidate.First the output should come as percentage and then keywords missing and last final thoughts.
    """

    input_prompt4 = input_prompt1 + input_prompt2 + input_prompt3

    if submit1:
        if uploaded_file is not None:
            pdf_content=input_pdf_setup(uploaded_file)
            response=get_gemini_response(input_prompt1,pdf_content,input_text)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.write("Please uplaod the resume")

    elif submit2:
        if uploaded_file is not None:
            pdf_content=input_pdf_setup(uploaded_file)
            response=get_gemini_response(input_prompt2,pdf_content,input_text)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.write("Please uplaod the resume")

    elif submit3:
        if uploaded_file is not None:
            pdf_content=input_pdf_setup(uploaded_file)
            response=get_gemini_response(input_prompt3,pdf_content,input_text)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.write("Please uplaod the resume")
    if submit4:
        if uploaded_file is not None:
            pdf_content=input_pdf_setup(uploaded_file)
            response=get_gemini_response(input_prompt4,pdf_content,input_text+submit4)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.write("Please uplaod the resume")
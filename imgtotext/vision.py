
import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image


import os
os.environ['GEMINI_API_KEY'] = 'AIzaSyDrdPBwWTuCPJ7JKekxJQDFPuCGCly-AB0'


import google.generativeai as genai
genai.configure(api_key=os.environ['GEMINI_API_KEY'])


## Function to load OpenAI model and get respones

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title=" Image to Text ")
st.header(' :red[img]2:green[text]')
st.header("IMAGE TO TEXT GENERATION")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Explain me about the image")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)


# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #211e40;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>Created By Abhisek Abhipsita</p>
        <a href="https://www.linkedin.com/in/abhisekabhipsita/" target="_blank">LINKEDIN</a>
        
    </div>
    """,
    unsafe_allow_html=True
)

from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os

# Load environment variables from .env
load_dotenv()

# Configure Streamlit
st.set_page_config(
    page_title="Generative AI Question Answering",
    page_icon=" :robot_face:",
    layout="wide"
)

# Load API key
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("GOOGLE_API_KEY not found. Please add it to the .env file.")
    st.stop()

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Function to generate content
def gen(question):
    response = model.generate_content(question)
    return response.text

# Streamlit app layout
st.title("Generative AI Question Answering")
st.markdown(
    """
    Welcome to the Gemini Powered Question Answering App.
    """
)

# User input for question
input_question = st.text_input('Input your question here:')

# Button to trigger question answering
submit_button = st.button('Submit')

# Generate and display response on button click
if submit_button:
    response_text = gen(input_question)
    st.write("Generated Response:")
    st.write(response_text)
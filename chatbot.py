# to use .env file
from dotenv import load_dotenv
load_dotenv()

#  to create website
import streamlit as st

import os

# to use gemini
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini pro model and get response
model = genai.GenerativeModel("gemini-pro")
# history=[] to store chat history
chat = model.start_chat(history=[])

# function to get response from gemini
def get_response(user_input):
    # store gemini response for a user input, stream=True to stream the response to display it later
    response = chat.send_message(user_input, stream=True)
    return response

#  set page configurations
st.set_page_config(page_title="Gemini Chatbot", layout="centered")

st.header("Gemini chatbot..")
st.subheader("Enter your quesries to get the solution ")

# using streamlit to store session history... adding a key-value pair in session_state 
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
    
# now the actual front-end
user_input = st.text_input("Enter your prompt here :", key="input")
submit = st.button("Enter")

if submit and input:
    response = get_response(user_input)
    
    # Add the user prompt and the gremini response to it to the chat area
    st.session_state['chat_history'].append(("You", user_input))
    st.subheader("The response is - ")
    for resp in response:
        st.write(resp.text)
        st.session_state['chat_history'].append(("Bot", resp.text))
st.subheader("The chat history is here : ")

for role, text in st.session_state['chat_history']:
    st.write(f"{role} : {text}")
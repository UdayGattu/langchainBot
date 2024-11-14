import requests
import streamlit as st

def get_openai_response(input_text):
    try:
        response = requests.post("http://localhost:8000/essay/invoke", json={'input': {'topic': input_text}})
        return response.json().get('output', {}).get('content', 'No content available')
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def get_ollama_response(input_text):
    try:
        response = requests.post("http://localhost:8000/poem/invoke", json={'input': {'topic': input_text}})
        return response.json().get('output', 'No content available')
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

st.title("LangChain Demo with LLAMA2 API")
input_text = st.text_input("write an essay on")
input_text1 = st.text_input("write an poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))

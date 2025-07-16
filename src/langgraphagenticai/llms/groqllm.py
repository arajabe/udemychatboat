import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input
        
    def get_llm_model(self):
        """
        Get the Groq LLM model based on user input.
        """
        try:
            groq_api_key = self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model = self.user_controls_input["select_model"]

            if groq_api_key == '' or os.getenv('GROQ_API_KEY') == '':
                st.error("Please enter a valid Groq API key.")
            llm = ChatGroq(model=selected_groq_model,groq_api_key=groq_api_key)

        except Exception as e:
            raise ValueError(f"Error initializing Groq LLM: {e}")   
        return llm
    




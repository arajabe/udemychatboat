import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import UIConfigFile

class LoadStreamlitUI:

    def __init__(self):
        self.config = UIConfigFile()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout='wide')
        st.header(self.config.get_page_title())
        
        # Display the page title
        st.title(self.config.get_page_title())
        
        # Create a sidebar for user controls
        with st.sidebar:
            # get LLM options from config
            llm_options = self.config.get_llm_options() 
            usecase_options = self.config.get_use_case_options()

            # Create a selectbox for LLM options
            self.user_controls['select_llm'] = st.selectbox('Select LLM', llm_options)
            
            if self.user_controls['select_llm'] == 'Groq':
                # model options for Groq
                model_options = self.config.get_groq_model()
                self.user_controls['select_model'] = st.selectbox('Select Model', model_options)
                self.user_controls['GROQ_API_KEY'] = st.session_state['GROQ_API_KEY']= st.text_input('API Key', type='password')
                
            if not self.user_controls['GROQ_API_KEY']:
                st.warning('Please enter your Groq API key to use the Groq model.')

            ## Use Case Selection
            self.user_controls['selected_usecase'] = st.selectbox('Select Use Case', usecase_options)
        
        return self.user_controls
    


      

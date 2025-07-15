import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """
    Load the LangGraph Agentic AI UI using Streamlit.
    """

    ## Load UI
    load_ui = LoadStreamlitUI()
    user_input = load_ui.load_streamlit_ui()
    
    if not user_input:
        st.error("Failed to load user controls. Please check the configuration.")
        return  
    
    user_message = st.chat_input("Enter your message:")
    


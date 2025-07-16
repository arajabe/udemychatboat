import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import json


class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph      
        self.user_message = user_message
    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph  
        user_message = self.user_message
        print(user_message)
        print(usecase)

        if usecase == 'Basic Chatbot':
            print("Displaying result for basic chatbot")
            for event in graph.stream({"messages":("user", user_message) }):
                print(event.values())
                for value in event.values():                
                    with st.chat_message(value['role']):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(value['messages'].content)
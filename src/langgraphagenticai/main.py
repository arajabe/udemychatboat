import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.llms.groqllm import GroqLLM
from src.langgraphagenticai.graph.builder_graph import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.displayui import DisplayResultStreamlit

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

    
    if user_message:

        ## configiure llm

        try:
            obj_llm_config = GroqLLM(user_input)
            model = obj_llm_config.get_llm_model()
            print("model")

        except Exception as e:
            st.error(f"Error initializing LLM model: {e}")
            return

        if not model:
            st.error("Failed to initialize the LLM model.")
            return
        ## Initialize and setup the graph based on use case
        usecase = user_input.get('selected_usecase')
        print(f"Selected use case: {usecase}")

        if not usecase:
            st.error("Please select a valid use case.")
            return
        
        ## Graph builder

        graph = GraphBuilder(model)
        try:
            graph_instance = graph.setup_graph(usecase)
            DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            if not graph_instance:
                st.error("Failed to setup the graph. Please check the use case configuration.")
                return

        except ValueError as e:
            st.error(f"Error initializing LLM: {e}")
            return




    


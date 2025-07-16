from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import GraphState
from src.langgraphagenticai.nodes.basic_chatboat import BasicChatbotNode



class GraphBuilder:   
    
    """
    BuilderGraph is a specialized StateGraph for building LangGraph Agentic AI applications.
    It extends the StateGraph to include specific configurations and methods for managing the application state.
    """
    def __init__(self, model):
        self.graph = StateGraph(GraphState)
        self.llm = model

    def basic_chatbot_build_graph(self):
        """
        Defines a basic chatbot flow in the graph.
        This method sets up the initial state and transitions for a simple chatbot interaction.

        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        
        self.graph.add_node("chatboat", self.basic_chatbot_node.process)
        
        print("Basic Chatbot node start")
        
        # Define the transition from START to END
        self.graph.add_edge(START, "chatboat")
        self.graph.add_edge("chatboat", END)
        print("self.graph")

        return self.graph
    
    def setup_graph(self, usecase):
        """
        Setup the graph based on the selected use case.
        
        :param usecase: The use case selected by the user.
        :return: The configured graph for the specified use case.
        """
        if usecase == "Basic Chatbot":
            print("setup graph")
            self.basic_chatbot_build_graph()
        return self.graph.compile()
        
       
        
        

    
    
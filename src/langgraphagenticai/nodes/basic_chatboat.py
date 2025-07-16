from src.langgraphagenticai.state.state import GraphState

class BasicChatbotNode:
    """
    A simple chatbot node that can respond to user input.
    This node can be used in a LangGraph Agentic AI application to handle basic interactions.
    """
    def __init__(self, model):
        self.model = model

    def process (self, state: GraphState) -> dict:
        """
        Process the user input and generate a response using the model.
        """
        print("process")
        message = state['messages']
        print(type(message))
       
        return {"messages": self.model.invoke("hello world")}

  
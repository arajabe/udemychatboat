from typing import Annotated,Sequence,Literal,List
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

class GraphState(TypedDict):
    """
    Represents the state of the LangGraph Agentic AI application.
    This state is used to manage the conversation history and user input.
    It is a TypedDict to ensure type safety and clarity in the structure.
    """
    messages: Annotated[List, add_messages]
   
from typing import Annotated,Sequence,Literal,List
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

class GraphState(TypedDict):
    """
    Represents the strecure of the used in graph.

    """
    print(" messages")
    message: Annotated[List, add_messages]
   
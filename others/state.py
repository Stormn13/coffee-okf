from typing import TypedDict, Literal, NotRequired

class State(TypedDict):
    initial_question : str 
    tag : NotRequired[list[Literal['coffee', 'hot', 'cold', 'milk', 'menu', 'policy', 'staff', 'hardware', 'operations']]] 
    selected_file : NotRequired[str]
    output: NotRequired[str]



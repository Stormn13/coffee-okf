from typing import TypedDict, Literal

class State(TypedDict):
    initial_question : str
    tag : list[Literal['coffee', 'hot', 'cold', 'milk', 'menu', 'policy', 'staff', 'hardware', 'operations']]
    selected_file : str
    output: str



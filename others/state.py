from typing import TypedDict, Literal

class State(TypedDict):
    initial_question : str
    tag : Literal['coffee', 'hot', 'cold', 'milk', 'menu', 'policy', 'staff', 'hardware', 'operations']
    output: str



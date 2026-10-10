from pydantic import BaseModel, Field
from typing import Literal

# Defined separately for cleaner code
FilterType = Literal['coffee', 'hot', 'cold', 'milk', 'menu', 'policy', 'staff', 'hardware', 'operations']

class filter_output(BaseModel):
    filters: list[FilterType] = Field(
        min_length=2,
        max_length=2,
        description="Analyze the question and select exactly 2 to 3 filters that suit this question the best."
    )
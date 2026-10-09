from pydantic import BaseModel, Field
from typing import Literal

class filter_output(BaseModel):
    filters: Literal['coffee', 'hot', 'cold', 'milk', 'menu', 'policy', 'staff', 'hardware', 'operations'] = Field(description="look at this question and then tell me what filters suit this question the best")
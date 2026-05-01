from pydantic import BaseModel

class Crop(BaseModel):
    name: str
    growth_time: int
    calories: int

class FamilyState(BaseModel):
    id: str
    inventory: list
    nutrition_score: float

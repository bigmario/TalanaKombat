from pydantic import BaseModel
from typing import List

class Player(BaseModel):
    movimientos: List[str] 
    golpes: List[str] 

class FightSchema(BaseModel):
    player1: Player
    player2: Player
    
    class Config:
        schema_extra = {
            "example": {
                "player1": {
                "movimientos": ["D", "DSD", "S", "DSD", "SD"],
                "golpes": ["K", "P", "", "K", "P"],
                },
                "player2": {
                    "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
                    "golpes": ["K", "", "K", "P", "P"],
                },
            },
        }
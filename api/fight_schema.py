from pydantic import BaseModel
from typing import List

class Player(BaseModel):
    movimientos: List[str] 
    golpes: List[str] 

class FightSchema(BaseModel):
    player1: Player
    player2: Player
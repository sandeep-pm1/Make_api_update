from pydantic import BaseModel
from typing import List, Optional

class Card(BaseModel):
    batchNumber : str
    brandName : str
    manufactureStage : str
    imageLink : str
    status : str
    events : list

class BatchDetail(BaseModel):
    name : str
    id : int
    cardList : Optional[List[Card]]
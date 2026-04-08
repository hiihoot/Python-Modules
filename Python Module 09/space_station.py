from pydantic import
from typing import Optional
from datetime import datetime



class SpaceStation(BaseModel):
    station_id: str = Field()
    name: str 
    crew_size: int
    power_level: float 
    oxygen_level: float
    last_maintenance: datetime
    is_operational: bool
    notes: Optional[str]    
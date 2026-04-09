from pydantic import Field, BaseModel, ValidationError, model_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CADET= "cadet"
    OFFICER= "officer"
    LIEUTENANT= "lieutenant"
    CAPTAIN= "captain"
    COMMANDER= "commander"



class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=10)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = datetime.now()
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(ge=1, le=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_rules(self):
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        
from pydantic import Field, BaseModel, ValidationError, model_validator
from typing import List, Dict
from datetime import datetime
from enum import Enum


class Rank(str, Enum):
    CADET = "cadet"
    COMMANDER = "commander"
    LIEUTENANT = "lieutenant"
    OFFICER = "officer"
    CAPTAIN = "captain"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_rules(self):
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        there_is: bool = False
        for person in self.crew:
            if (
                person.rank == Rank.CAPTAIN or
                person.rank == Rank.COMMANDER
            ):
                there_is = True
        if not there_is:
            raise ValueError("must have at least one commander or captain")
        if self.duration_days > 365:
            exp_counter: int = 0
            for person in self.crew:
                if person.years_experience >= 5:
                    exp_counter += 1

            if exp_counter < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) "
                    "need 50% experienced crew (5+ years)"
                )

        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("========================================")
    try:
        crew: List[CrewMember] = []
        members: Dict[str, List] = {
            'Sarah Connor': [Rank.COMMANDER, 43, "engineer", 23],
            'John Smith': [Rank.LIEUTENANT, 45, "engineer", 43],
            'Alice Johnson': [Rank.OFFICER, 65, "engineer", 23],
            'James keneddy': [Rank.OFFICER, 54, "engineer", 43],
            'Leon Scott': [Rank.CADET, 46, "engineer", 4],
            'Jack Kraouser': [Rank.CADET, 46, "engineer", 2],
            'Tommas Brown': [Rank.CADET, 46, "engineer", 23],
            'Edward Martiniz': [Rank.CADET, 36, "engineer", 6],
        }
        id: int = 0
        for name, data in members.items():
            crw: CrewMember = CrewMember(
                member_id=f"CM_00{110+id}",
                name=name,
                rank=data[0],
                age=data[1],
                specialization=data[2],
                years_experience=data[3],
                is_active=True
            )
            id += 1
            crew.append(crw)
        mission: SpaceMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2028, 10, 1),
            duration_days=900,
            crew=crew[:3],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for c in mission.crew:
            print(f" - {c.name} ({c.rank}) - ", end="")
            if c.rank == Rank.COMMANDER:
                print('Mission Command')
            elif c.rank == Rank.LIEUTENANT:
                print('Navigation')
            elif c.rank == Rank.OFFICER:
                print('Engineering')
            else:
                print('Unknown')
        print("\n========================================")
        print("Expected validation error:")
        SpaceMission(
            mission_id="Msomethng",
            mission_name="some place",
            destination="earth",
            launch_date=datetime(2026, 11, 1),
            duration_days=123,
            crew=crew[4:7],
            budget_millions=80.5
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'].replace('Value error, ', ''))


if __name__ == "__main__":
    main()

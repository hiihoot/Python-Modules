from pydantic import Field, BaseModel, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(le=datetime.now())
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(None, max_length=200)


def main():
    print("\nSpace Station Data Validation")
    print("========================================")
    try:
        valid = SpaceStation(
            station_id="QCH1819",
            name="IDeep Space Observatory",
            crew_size=3,
            power_level=70.8,
            oxygen_level=88.1,
            last_maintenance=datetime(2026, 1, 11),
            is_operational=False,
            notes="System diagnostics required"
        )
        print("Valid station created:")
        print(f"ID: {valid.station_id}")
        print(f"Name: {valid.name}")
        print(f"Crew: {valid.crew_size} people")
        print(f"Power: {valid.power_level}%")
        print(f"Oxygen: {valid.oxygen_level}%")
        status = "Operational" if valid.is_operational else "Down"
        print(f"Status: {status}")
        print("========================================")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])
    try:
        valid = SpaceStation(
            station_id="QCH1819",
            name="IDeep Space Observatory",
            crew_size=80,
            power_level=70.8,
            oxygen_level=88.1,
            last_maintenance=datetime(2026, 1, 11),
            is_operational=False,
            notes="System diagnostics required"
        )
        print("========================================")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()

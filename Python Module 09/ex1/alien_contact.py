from pydantic import Field, BaseModel, ValidationError, model_validator
from typing import Optional
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def rules_check(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')

        if (
            self.contact_type == ContactType.TELEPATHIC and
            self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
                )

        return self


def main():
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        valid = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Atacama Desert, Chile",
            contact_type=ContactType.VISUAL,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )

        print("Valid contact report:")
        print(f"ID: {valid.contact_id}")
        print(f"Type: {valid.contact_type.value}")
        print(f"Location: {valid.location}")
        print(f"Signal: {valid.signal_strength}/10")
        print(f"Durat ion: {valid.duration_minutes} minutes")
        print(f"Witnesses: {valid.witness_count}")
        print(f"Message: '{valid.message_received}'")
        print()
        print("======================================")
    except ValidationError as e:
        print(e.errors()[0]["msg"].replace("Value error, ", ""))

    try:
        valid = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Atacama Desert, Chile",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()

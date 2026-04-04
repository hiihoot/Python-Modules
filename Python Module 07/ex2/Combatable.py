from abc import ABC, abstractmethod


class Combatable(ABC):
    @abstractmethod
    def attack(self, target: str) -> dict: ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict: ...

    def get_combat_stats(self) -> dict: ...

    get_combat_stats = abstractmethod(get_combat_stats)

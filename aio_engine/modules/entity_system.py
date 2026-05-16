from dataclasses import dataclass


@dataclass
class Entity:
    entity_id: str
    kind: str
    x: float
    y: float
    hp: int


class EntitySystem:
    def from_scene_entities(self, entities: list[dict]) -> list[Entity]:
        return [Entity(e["id"], e["kind"], e["x"], e["y"], e["hp"]) for e in entities]

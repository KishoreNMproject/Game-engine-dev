from dataclasses import dataclass, field
from typing import Any


@dataclass
class GameIntent:
    raw_prompt: str
    genre: str = "survival"
    biome: str = "forest"
    weather: str = "clear"
    enemies: list[str] = field(default_factory=list)
    mechanics: list[str] = field(default_factory=lambda: ["movement", "health", "collision"])


@dataclass
class SceneSpec:
    map_type: str
    weather: str
    entities: list[dict[str, Any]]
    systems: list[str]
    metadata: dict[str, Any] = field(default_factory=dict)

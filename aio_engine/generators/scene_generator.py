import json
from pathlib import Path

from aio_engine.core.models import GameIntent, SceneSpec


class SceneGenerator:
    def generate(self, intent: GameIntent, systems: list[str]) -> SceneSpec:
        entities = [
            {"id": "player", "kind": "player", "x": 100, "y": 100, "hp": 100},
        ]
        for i, enemy in enumerate(intent.enemies or ["wolf"]):
            entities.append(
                {"id": f"{enemy}_{i}", "kind": enemy, "x": 240 + i * 60, "y": 180, "hp": 40}
            )

        return SceneSpec(
            map_type=intent.biome,
            weather=intent.weather,
            entities=entities,
            systems=systems,
            metadata={"genre": intent.genre, "source_prompt": intent.raw_prompt},
        )

    def save(self, spec: SceneSpec, path: Path) -> None:
        payload = {
            "map_type": spec.map_type,
            "weather": spec.weather,
            "entities": spec.entities,
            "systems": spec.systems,
            "metadata": spec.metadata,
        }
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

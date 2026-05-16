import json
from pathlib import Path

from aio_engine.core.models import GameIntent


class PromptInterpreter:
    """Transforms natural language into structured intent."""

    KEYWORDS = {
        "snow": ("biome", "snow"),
        "forest": ("biome", "forest"),
        "rain": ("weather", "rain"),
        "dark fantasy": ("genre", "dark_fantasy"),
    }

    def interpret(self, prompt: str) -> GameIntent:
        prompt_lower = prompt.lower()
        intent = GameIntent(raw_prompt=prompt)

        for key, (field, value) in self.KEYWORDS.items():
            if key in prompt_lower:
                setattr(intent, field, value)

        if "wolf" in prompt_lower:
            intent.enemies.append("wolf")

        if "craft" in prompt_lower:
            intent.mechanics.append("crafting")

        if "inventory" not in intent.mechanics:
            intent.mechanics.append("inventory")

        return intent

    def save_intent(self, intent: GameIntent, path: Path) -> None:
        payload = {
            "raw_prompt": intent.raw_prompt,
            "genre": intent.genre,
            "biome": intent.biome,
            "weather": intent.weather,
            "enemies": intent.enemies,
            "mechanics": intent.mechanics,
        }
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

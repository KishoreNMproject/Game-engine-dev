from aio_engine.core.models import GameIntent


class AIPlanningLayer:
    """Maps intent into modular systems plan."""

    BASE_SYSTEMS = [
        "entity_system",
        "physics_collision",
        "inventory_system",
        "weather_system",
        "enemy_ai",
        "health_system",
    ]

    def build_plan(self, intent: GameIntent) -> list[str]:
        systems = list(self.BASE_SYSTEMS)
        if "crafting" in intent.mechanics:
            systems.append("crafting_system")
        return systems

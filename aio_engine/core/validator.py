class ValidationError(Exception):
    pass


class ValidationLayer:
    REQUIRED_KEYS = {"map_type", "weather", "entities", "systems", "metadata"}

    def validate_scene_dict(self, scene: dict) -> None:
        missing = self.REQUIRED_KEYS - set(scene.keys())
        if missing:
            raise ValidationError(f"Missing scene keys: {sorted(missing)}")
        if not scene["entities"]:
            raise ValidationError("Scene must include at least one entity.")

import pygame


class AssetLoader:
    """Placeholder loader for future sprites/sounds; currently color-based rendering."""

    def color_for(self, kind: str) -> tuple[int, int, int]:
        return {
            "player": (40, 220, 80),
            "wolf": (170, 170, 170),
        }.get(kind, (240, 240, 240))

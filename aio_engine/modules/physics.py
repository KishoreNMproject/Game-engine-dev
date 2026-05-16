import pygame


class PhysicsCollisionLayer:
    def build_rect(self, x: float, y: float, size: int = 24) -> pygame.Rect:
        return pygame.Rect(int(x), int(y), size, size)

    def clamp_to_world(self, rect: pygame.Rect, world_w: int, world_h: int) -> None:
        rect.x = max(0, min(rect.x, world_w - rect.width))
        rect.y = max(0, min(rect.y, world_h - rect.height))

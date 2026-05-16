import pygame


class WeatherSystem:
    def __init__(self, weather: str) -> None:
        self.weather = weather

    def render_overlay(self, surface: pygame.Surface) -> None:
        if self.weather == "rain":
            overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
            overlay.fill((50, 90, 140, 50))
            surface.blit(overlay, (0, 0))
        elif self.weather == "snow":
            overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
            overlay.fill((220, 220, 255, 50))
            surface.blit(overlay, (0, 0))

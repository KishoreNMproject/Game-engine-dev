import argparse
import json
from pathlib import Path

import pygame

from aio_engine.ai.planner import AIPlanningLayer
from aio_engine.ai.prompt_interpreter import PromptInterpreter
from aio_engine.core.validator import ValidationLayer
from aio_engine.generators.scene_generator import SceneGenerator
from aio_engine.modules.assets import AssetLoader
from aio_engine.modules.enemy_ai import BasicEnemyAI
from aio_engine.modules.entity_system import EntitySystem
from aio_engine.modules.inventory import InventorySystem
from aio_engine.modules.physics import PhysicsCollisionLayer
from aio_engine.modules.weather import WeatherSystem


def generate_scene_from_prompt(prompt: str, root: Path) -> dict:
    interpreter = PromptInterpreter()
    planner = AIPlanningLayer()
    generator = SceneGenerator()
    validator = ValidationLayer()

    intent = interpreter.interpret(prompt)
    interpreter.save_intent(intent, root / "prompts" / "latest_prompt.json")

    systems = planner.build_plan(intent)
    spec = generator.generate(intent, systems)
    generator.save(spec, root / "scenes" / "generated_scene.json")

    scene_dict = json.loads((root / "scenes" / "generated_scene.json").read_text(encoding="utf-8"))
    validator.validate_scene_dict(scene_dict)
    return scene_dict


def run_game(scene: dict) -> None:
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("AIO Engine MVP")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    entities = EntitySystem().from_scene_entities(scene["entities"])
    player = next(e for e in entities if e.kind == "player")
    enemies = [e for e in entities if e.kind != "player"]

    physics = PhysicsCollisionLayer()
    assets = AssetLoader()
    ai = BasicEnemyAI()
    weather = WeatherSystem(scene["weather"])
    inventory = InventorySystem()

    player_rect = physics.build_rect(player.x, player.y)
    player_hp = player.hp

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_rect.y -= 3
        if keys[pygame.K_s]:
            player_rect.y += 3
        if keys[pygame.K_a]:
            player_rect.x -= 3
        if keys[pygame.K_d]:
            player_rect.x += 3
        physics.clamp_to_world(player_rect, 800, 500)

        for enemy in enemies:
            ai.tick(enemy, player_rect)
            enemy_rect = physics.build_rect(enemy.x, enemy.y)
            if enemy_rect.colliderect(player_rect):
                player_hp = max(0, player_hp - 1)
                inventory.add_item("meat", 1)

        bg = (40, 90, 40) if scene["map_type"] == "forest" else (180, 180, 210)
        screen.fill(bg)

        pygame.draw.rect(screen, assets.color_for("player"), player_rect)
        for enemy in enemies:
            pygame.draw.rect(screen, assets.color_for(enemy.kind), physics.build_rect(enemy.x, enemy.y))

        weather.render_overlay(screen)
        hud = font.render(f"HP: {player_hp}  Inventory: {inventory.items}", True, (255, 255, 255))
        screen.blit(hud, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def main() -> None:
    parser = argparse.ArgumentParser(description="AIO Engine MVP runtime")
    parser.add_argument("--prompt", default="Forest survival game with rain and wolves.")
    parser.add_argument("--no-run", action="store_true", help="Only generate scene, skip pygame runtime")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    scene = generate_scene_from_prompt(args.prompt, root)
    if not args.no_run:
        run_game(scene)


if __name__ == "__main__":
    main()

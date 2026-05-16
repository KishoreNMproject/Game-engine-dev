# AIO Engine (Experimental MVP)

AIO Engine is an experimental AI-powered modular game development engine that converts natural-language prompts into small playable 2D indie prototypes.

## Workflow

`User Prompt -> Prompt Interpreter -> AI Planning Layer -> Modular Assembly -> Playable Game`

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install pygame
python -m aio_engine.runtime.main --prompt "Forest survival game with rain and wolves."
```

## Current MVP Features

- Prompt-to-JSON interpretation.
- Scene generator producing structured data under `aio_engine/scenes/`.
- Modular systems: entity, inventory, weather, combat, enemy AI, collision.
- Minimal playable prototype using pygame.
- Validation layer for generated scene specs.

## Output

Running with a prompt generates:

1. `aio_engine/prompts/latest_prompt.json`
2. `aio_engine/scenes/generated_scene.json`
3. Playable pygame loop with player + wolves + weather overlays.

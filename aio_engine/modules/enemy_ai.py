class BasicEnemyAI:
    def tick(self, enemy, player_rect) -> None:
        if enemy.x < player_rect.x:
            enemy.x += 0.4
        elif enemy.x > player_rect.x:
            enemy.x -= 0.4
        if enemy.y < player_rect.y:
            enemy.y += 0.4
        elif enemy.y > player_rect.y:
            enemy.y -= 0.4

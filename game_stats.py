class GameStats():
    """Отслеживание статистики для игры"""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.high_score = 0
        self.reset_stats()

        # Игра запускается в неактивном состоянии
        self.game_active = False

    def reset_stats(self):
        """Сбрасывает статистику"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
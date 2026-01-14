from pathlib import Path


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Read all time high score from the file
        path = Path("highscore.txt")
        if path.exists():
            contents = path.read_text(encoding="utf-8").strip()
            self.high_score = int(contents) if contents else 0
        else:
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

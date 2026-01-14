class GameStats:
    """Track statistics for game."""

    def __init__(self, game):
        """Initialize statistics."""
        self.settings = game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Reset statistics."""
        self.rockets_left = self.settings.rocket_limit
        self.score = 0
        self.level = 1

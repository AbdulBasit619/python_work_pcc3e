class GameStats:
    """Track statistics for game."""

    def __init__(self, game):
        """Initialize statistics."""
        self.settings = game.settings
        self.reset_stats()

    def reset_stats(self):
        """Reset statistics."""
        self.rockets_left = self.settings.rocket_limit

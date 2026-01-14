class Settings:
    """Create settings for the star grid"""

    def __init__(self):
        """Initialize the grid's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 10, 40)

        # Fraction of a star's size used as maximum random offset (0.0 - 1.0)
        # e.g., 0.5 allows up to half the star's width/height offset
        self.star_jitter_factor = 0.5

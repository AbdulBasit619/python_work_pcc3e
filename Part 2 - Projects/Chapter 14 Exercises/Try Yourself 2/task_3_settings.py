class Settings:
    """A class to store all settings for Task 2."""

    def __init__(self):
        """Initialize settings for the game."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 500
        self.bg_color = (10, 10, 50)

        # Rectangle Settings
        self.rectangle_width = 12
        self.rectangle_height = 80
        self.rectangle_color = (180, 0, 200)

        # Rocket settings
        self.rocket_speed = 4.0

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (0, 180, 50)
        self.bullet_speed = 2.5
        self.bullets_allowed = 3

        # Rectangle Speed Up Scale
        self.speedup_scale = 1.01

        self._initialize_dynamic_settings()

    def _initialize_dynamic_settings(self):
        """Initialize dynamic settings of the game."""
        # Rectangle Settings
        self.rectangle_direction = 1
        self.rectangle_speed = 2.0
        self.max_rectangle_speed = 20.0

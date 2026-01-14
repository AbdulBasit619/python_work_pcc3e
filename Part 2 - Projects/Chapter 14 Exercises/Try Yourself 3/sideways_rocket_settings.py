class Settings:
    """Class to store all the settings for the Sideways Rocket Game."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 40, 40)

        # Rocket Settings
        self.rocket_limit = 3

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 1000
        self.bullet_color = (220, 50, 50)
        self.bullet_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 30

        # How quickly the game scales up.
        self.speedup_scale = 1.1
        self.score_scale = 1.5

    def _initialize_dynamic_settings(self):
        """Initialize dynamic settings of the game."""
        self.rocket_speed = 2.0
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # Fleet direction of 1 indicates bottom, -1 indicates top.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def _increase_speed(self):
        """Increase the speed settings."""
        self.rocket_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

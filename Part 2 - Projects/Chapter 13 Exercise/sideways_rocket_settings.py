class Settings:
    """Class to store all the settings for the Sideways Rocket Game."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 40, 40)

        # Rocket Settings
        self.rocket_speed = 2.0
        self.rocket_limit = 3

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (220, 50, 50)
        self.bullet_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 30

        # Fleet direction of 1 indicates bottom, -1 indicates top.
        self.fleet_direction = 1

class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 10, 10)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 2000
        self.bullet_height = 15
        self.bullet_color = (150, 40, 40)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game scales up.
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        # Difficulty settings
        self.difficulty = 0

        self._initialize_dynamic_settings()

    def _initialize_dynamic_settings(self):
        """Initialize the game's dynamic settings"""

        if self.difficulty == 0:
            self.set_easy()
        elif self.difficulty == 1:
            self.set_medium()
        elif self.difficulty == 2:
            self.set_hard()

        # Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def set_easy(self):
        self.difficulty = 0
        self.ship_speed = 3.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.25
        self.alien_points = 50
        self.speedup_scale = 1.1

    def set_medium(self):
        self.difficulty = 1
        self.ship_speed = 4.0
        self.bullet_speed = 4.5
        self.alien_speed = 1.50
        self.alien_points = 75
        self.speedup_scale = 1.2

    def set_hard(self):
        self.difficulty = 2
        self.ship_speed = 5.0
        self.bullet_speed = 6.0
        self.alien_speed = 3.0
        self.alien_points = 100
        self.speedup_scale = 1.3

    def increase_speed(self):
        """Increase speed settings and alien point values."""

        if self.ship_speed < 20:
            self.ship_speed *= self.speedup_scale
        if self.bullet_speed < 15:
            self.bullet_speed *= self.speedup_scale
        if self.alien_speed < 10:
            self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

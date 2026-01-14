import pygame.mixer as mx


class SoundEffects:
    """A class to manage all sound effects of the game."""

    def __init__(self, ai_game):
        """Load the sound and initialize properties."""
        mx.init()
        self.settings = ai_game.settings

        # Load sounds
        self._shoot = mx.Sound("sfx/bullet.wav")
        self._alien_hit = mx.Sound("sfx/alien.wav")
        self._ship_hit = mx.Sound("sfx/ship.wav")

        # Adjust the sound volume
        self._shoot.set_volume(self.settings.shoot_sound)
        self._alien_hit.set_volume(self.settings.alien_hit_sound)
        self._ship_hit.set_volume(self.settings.ship_hit_sound)

    def play_shoot(self):
        """Play the sound when a bullet is fired."""
        self._shoot.play()

    def play_alien_hit(self):
        """Play the sound when an alien is hit."""
        self._alien_hit.play()

    def play_ship_hit(self):
        """Play the sound when ship is hit."""
        self._ship_hit.play()

import pygame.font


class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg):
        """Initialize button settings."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50

        self.button_color = (0, 100, 100)
        self.highlight_color = (180, 100, 50)
        self.text_color = self.settings.bg_color

        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Selection state
        self.selected = False

        # The message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn message into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self, enabled=True):
        """Draw blank button and then draw message."""
        color = self.highlight_color if self.selected else self.button_color
        if not enabled:
            color = (120, 120, 120)
        self.screen.fill(color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

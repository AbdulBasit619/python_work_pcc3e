from pygame.sprite import Group
import pygame.font

from sideways_rocket import SidewaysRocket


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, game):
        """Initialize scorekeeping attributes."""
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # Font settings for scoring information
        self.text_color = (50, 50, 220)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_rockets()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_highscore(self):
        """Turn high score into a rendered image."""
        highscore = round(self.stats.high_score, -1)
        highscore_str = f"{highscore:,}"
        self.highscore_image = self.font.render(
            highscore_str, True, self.text_color, self.settings.bg_color
        )

        # Position high score on the topleft of the screen
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.left = 20
        self.highscore_rect.top = 20

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(
            str(self.stats.level), True, self.text_color, self.settings.bg_color
        )

        # Position level below the score.
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_rect.right
        self.level_image_rect.top = self.score_rect.bottom + 10

    def prep_rockets(self):
        """Show how many rockets are left."""
        self.rockets = Group()
        for rocket_number in range(self.stats.rockets_left):
            rocket = SidewaysRocket(self.game)
            rocket.rect.right = self.screen_rect.right - 20
            rocket.rect.bottom = self.screen_rect.bottom - (
                rocket_number * (rocket.rect.height + 10)
            )
            self.rockets.add(rocket)

    def show_score(self):
        """Draw score and level to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.rockets.draw(self.screen)

    def check_highscore(self):
        """Check to see if there is a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_highscore()

import sys

import pygame

# from settings import Settings
# from rocket import Rocket


# class Game:
#     """Overall class to manage the game."""

#     def __init__(self):
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Settings()
#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height)
#         )
#         pygame.display.set_caption("Rockets and Keys")
#         self.rocket = Rocket(self)

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             self._manage_events()
#             self.rocket.update()
#             self._update_screen()
#             self.clock.tick(60)

#     def _manage_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Check for key presses."""
#         if event.key == pygame.K_UP:
#             self.rocket.moving_up = True
#         elif event.key == pygame.K_RIGHT:
#             self.rocket.moving_right = True
#         elif event.key == pygame.K_DOWN:
#             self.rocket.moving_down = True
#         elif event.key == pygame.K_LEFT:
#             self.rocket.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()

#     def _check_keyup_events(self, event):
#         """Check for key releases"""
#         if event.key == pygame.K_UP:
#             self.rocket.moving_up = False
#         elif event.key == pygame.K_RIGHT:
#             self.rocket.moving_right = False
#         elif event.key == pygame.K_DOWN:
#             self.rocket.moving_down = False
#         elif event.key == pygame.K_LEFT:
#             self.rocket.moving_left = False

#     def _update_screen(self):
#         self.screen.fill(self.settings.bg_color)
#         self.rocket.blitme()

#         pygame.display.flip()


# if __name__ == "__main__":
#     game = Game()
#     game.run_game()


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    pygame.display.set_caption("Key Testing")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                print(event.key)

        # Fill and update the screen
        screen.fill((30, 30, 30))
        pygame.display.flip()


if __name__ == "__main__":
    run_game()

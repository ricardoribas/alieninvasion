import sys
import pygame

from Settings import Settings
from Ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        self.ship = Ship(self)

        pygame.display.set_caption('Alien Invasion')

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def update_screen(self):
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()

    def run_game(self):
        while True:
            self.check_events()
            self.ship.update()
            self.update_screen()

            pygame.display.flip()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()

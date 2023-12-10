import sys
import pygame
from setting import Setting
from ship import Ship


class AlianInvasion:
    def __init__(self):
        pygame.init()
        self.setting = Setting()

        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height)
        )
        pygame.display.set_caption("Alian Invasion")

        self.ship = Ship(self)


    def rungame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.setting.bg_color)

            self.ship.blitme()

            pygame.display.flip()


if __name__ == "__main__":
    ai = AlianInvasion()
    ai.rungame()

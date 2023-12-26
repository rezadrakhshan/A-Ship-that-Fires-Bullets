import pygame.font


class Scoreboard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.score_rect = self.screen.get_rect()
        self.settings = ai_game.setting
        self.stats = ai_game.stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )
        self.score_rect.right = self.score_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)

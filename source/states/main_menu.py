import pygame
from .. import setup, tools
from .. import constants as C


class MainMenu:
    def __init__(self):
        #设置底图
        self.setup_background()
        #设置玩家
        self.setup_player()
        #设置光标
        self.setup_cursor()

    def setup_background(self):
        self.background = setup.GRAPHICS['level_1']
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(
            self.background, (int(self.background_rect.width * C.BG_MULTI),
                              int(self.background_rect.height * C.BG_MULTI)))
        self.viewport = setup.SCREEN.get_rect()

        self.caption = tools.get_image(setup.GRAPHICS['title_screen'], 1, 60,
                                       176, 88, (255, 0, 220), C.BG_MULTI)

    def setup_player(self):
        self.player_image = tools.get_image(setup.GRAPHICS['mario_bros'], 178,
                                            32, 12, 16, (0, 0, 0),
                                            C.PLAYER_MULTI)

    def setup_cursor(self):
        self.cursor_image = tools.get_image(setup.GRAPHICS['item_objects'], 24,
                                            160, 8, 8, (0, 0, 0),
                                            C.PLAYER_MULTI)

    def update(self, surface):
        #import random
        #surface.fill((random.randint(0, 255), random.randint(0, 255),
        #random.randint(0, 255)))
        surface.blit(self.background, self.viewport)
        surface.blit(self.caption, (170, 100))
        surface.blit(self.player_image, (110, 490))
        surface.blit(self.cursor_image, (220, 360))

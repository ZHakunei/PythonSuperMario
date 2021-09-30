#   -*- coding:utf-8 -*-
#   @Time   :   2021/9/30 17:18
#   @Author :   ZHakunei
#   @Email  :   zhang_boning@outlook.com

import pygame
from ..components import info, player
from .. import setup, tools
from .. import constants as C


class Level:
    def __init__(self):
        self.finished = False
        self.next = None
        self.info = info.Info('level')
        self.setup_background()
        self.setup_player()

    def setup_background(self):
        self.background = setup.GRAPHICS['level_1']
        rect = self.background.get_rect()

        self.background = pygame.transform.scale(
            self.background, (int(rect.width * C.BG_MULTI),
                              int(rect.height * C.BG_MULTI)))
        self.background_rect = self.background.get_rect()
        #
        self.caption = tools.get_image(setup.GRAPHICS['title_screen'], 0, 59,
                                       177, 89, (255, 0, 220), C.BG_MULTI)

    def setup_player(self):
        self.player = player.Player('mario')
        self.player.rect.x = 300
        self.player.rect.y = 300

    def update(self, surface, keys):
        self.draw(surface)
        self.info.update()
        self.player.update(keys)
        self.update_player_position()

    def update_player_position(self):
        self.player.rect.x += self.player.x_vel
        self.player.rect.y += self.player.y_vel

    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        surface.blit(self.player.image, self.player.rect)
        self.info.draw(surface)

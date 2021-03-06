#   -*- coding:utf-8 -*-
#   @Time   :   2021/9/30 17:18
#   @Author :   ZHakunei
#   @Email  :   zhang_boning@outlook.com

import pygame
from ..components import info


class LoadScreen:
    def __init__(self):
        self.finished = False
        self.next = 'level'
        self.timer = 0
        self.info = info.Info('load_screen')

    def update(self, surface, keys):
        self.draw(surface)
        if self.timer == 0:
            self.timer = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - self.timer > 1000:
            self.finished = True
            self.timer = 0

        self.info.update()

    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.info.draw(surface)

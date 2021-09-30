#   -*- coding:utf-8 -*-
#   @Time   :   2021/9/30 17:18
#   @Author :   ZHakunei
#   @Email  :   zhang_boning@outlook.com

import pygame
from . import constants as C
from . import tools

print('Hello Boning')
pygame.init()
SCREEN = pygame.display.set_mode((C.SCREEN_W, C.SCREEN_H))
GRAPHICS = tools.load_graphics('resources/graphics')

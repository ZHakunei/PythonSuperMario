import pygame
from ..components import info
from .. import setup,tools
from .. import constants as C


class Level:
    def __init__(self):
        self.finished = False
        self.next = None
        self.info=info.Info('level')
        self.setup_background()

    def setup_background(self):
        self.background = setup.GRAPHICS['level_1']
        rect=self.background.get_rect()


        self.background = pygame.transform.scale(
            self.background, (int(rect.width * C.BG_MULTI),
                              int(rect.height * C.BG_MULTI)))
        self.background_rect=self.background.get_rect()
        #
        self.caption = tools.get_image(setup.GRAPHICS['title_screen'], 0, 59,
                                       177, 89, (255, 0, 220),C.BG_MULTI)
    def update(self, surface, keys):
        self.draw(surface)
        self.info.update()



    def draw(self, surface):
        #surface.fill((0,100,0))
        surface.blit(self.background, (0,0))
        self.info.draw(surface)
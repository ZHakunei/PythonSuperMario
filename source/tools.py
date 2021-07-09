import pygame
import random
import os

from pygame import image


class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def run(self,GRAPHICS):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.getpressed()
            self.screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            image = get_image(GRAPHICS['mario_bros'], 145, 32, 16, 16, (0, 0, 0), random.randint(5,15))
            self.screen.blit(image, (300, 300))
            pygame.display.update()
            self.clock.tick(1)

# 载入图片


def load_graphics(path, accept=('.jpg', '.png', '.bmp', '.gif')):
    # 创建一个字典
    graphics = {}
    # 遍历文件夹
    for pic in os.listdir(path):
        # 拆分文件名和后缀(extension)两个部分
        name, ext = os.path.splitext(pic)
        # 如果后缀是accept的格式
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, pic))
            # 如果图片有alpha层
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics

# colorkey是选中底色快速抠图


def get_image(sheet, x, y, width, height, colorkey, scale):
    image = pygame.Surface((width, height))
    image.blit(sheet, (0, 0), (x, y, width, height))
    image.set_colorkey(colorkey)
    image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
    return image

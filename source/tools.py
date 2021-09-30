#   -*- coding:utf-8 -*-
#   @Time   :   2021/9/30 17:18
#   @Author :   ZHakunei
#   @Email  :   zhang_boning@outlook.com

import pygame
import random
import os
from pygame import image


class Game:
    def __init__(self, state_dict, start_state):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        self.state_dict = state_dict
        self.state = self.state_dict[start_state]

    def update(self):
        if self.state.finished:
            next_state = self.state.next
            self.state.finished = False
            self.state = self.state_dict[next_state]
        self.state.update(self.screen, self.keys)  # state的update方法由MainMenu类定义

    def run(self, state):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            # self.screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            # image = get_image(GRAPHICS['mario_bros'], 145, 32, 16, 16, (0, 0, 0), random.randint(5,15))
            # self.screen.blit(image, (300, 300))
            self.update()
            pygame.display.update()
            self.clock.tick(20)


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
    image = pygame.transform.scale(image,
                                   (int(width * scale), int(height * scale)))
    return image

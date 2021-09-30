#   -*- coding:utf-8 -*-
#   @Time   :   2021/9/30 17:18
#   @Author :   ZHakunei
#   @Email  :   zhang_boning@outlook.com

import pygame
from source import tools, setup
from source.states import main_menu, load_screen, level


def main():
    state_dict = {
        'main_menu': main_menu.MainMenu(),
        'load_screen': load_screen.LoadScreen(),
        'level': level.Level()
    }
    game = tools.Game(state_dict, 'main_menu')
    state = main_menu.MainMenu()#state初始化为一个mainmenu的实例, 可以作为一个状态机, 使游戏运行到某个阶段
    game.run(state)#Game类下的run方法,传入state


if __name__ == '__main__':
    main()

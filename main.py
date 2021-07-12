import pygame
from source import tools, setup
from source.states import main_menu


def main():
    game = tools.Game()
    #state初始化为一个mainmenu的实例, 可以作为一个状态机, 使游戏运行到某个阶段
    state = main_menu.MainMenu()
    game.run(state)


if __name__ == '__main__':
    main()

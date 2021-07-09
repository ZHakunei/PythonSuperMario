import pygame
pygame.init()

# 设置画布宽高
w, h = 700, 500
pygame.display.set_mode((w, h))
# 获取屏幕图层,是一块画布 在上面画东西
screen = pygame.display.get_surface()

#读入图片, 然后scale
bgpic = pygame.image.load('bgpic.png')
bgpic = pygame.transform.scale(bgpic, (w, h))
# 读入马里奥
mario_image = pygame.image.load('mario.png')

# 创建精灵对象sprite
mario = pygame.sprite.Sprite()
mario.image = mario_image

# rect是Rectangle 矩形的缩写 可以改宽高 坐标
mario.rect = mario.image.get_rect()
# 坐标改到屏幕中心
mario.rect.x, mario.rect.y = w/2, h/2

# 玩家组
player_group = pygame.sprite.Group()
player_group.add(mario)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                mario.rect.y += 10
            if keys[pygame.K_UP]:
                mario.rect.y -= 10
            if keys[pygame.K_LEFT]:
                mario.rect.x -= 10
            if keys[pygame.K_RIGHT]:
                mario.rect.x += 10

    #画图, 用blit方法, 将背景图贴上
    screen.blit(bgpic, (0, 0))
    player_group.draw(screen)
    pygame.display.update()

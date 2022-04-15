#工具和游戏主控
import os

import pygame
import random

class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def run(self, GRAPHICS):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()

            state.update(self.screen)

            pygame.display.update()
            self.clock.tick(60)

def load_graphics(path, accept=('.jpg', '.png', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path,pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics

def get_image(sheet, x, y, width, height, colorkey,scale):
    image = pygame.Surface((width, height))
    image.blit(sheet, (0, 0), (x, y, width, height)) #0,0代表画到哪个位置，x,y,width,height代表sheet从哪个区域里取出来
    image.set_colorkey(colorkey) #抠图底色
    image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
    return image
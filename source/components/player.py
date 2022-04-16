import pygame
from .. import tools, setup
from .. import constants as C


class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.setup_states()
        self.setup_velocities()
        self.setup_timers()
        self.load_images()

    def setup_states(self):
        self.face_right = True
        self.dead = False
        self.big = False

    def setup_velocities(self):
        self.x_vel = 0
        self.y_vel = 0

    def setup_timers(self):
        self.walking_timer = 0
        self.transition_timer = 0

    def load_images(self):
        sheet = setup.GRAPHICS['mario_bros']
        self.frames = []
        self.frames.append(tools.get_image(sheet, 178, 32, 12, 16, (0, 0, 0), C.PLAYER_MULTI))

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def update(self, keys):
        if keys[pygame.K_RIGHT]:
            self.x_vel = 5
        if keys[pygame.K_LEFT]:
            self.x_vel = -5


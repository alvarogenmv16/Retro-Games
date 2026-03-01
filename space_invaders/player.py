import pygame
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, max_x, speed):
        super().__init__()
        self.image = pygame.image.load('../Graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.max_x = max_x
        self.speed = speed
        self.ready = True
        self.cooldown = 600
        self.laser_time = 0

        self.laser = pygame.sprite.Group()

    def get_player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.cooldown_time = pygame.time.get_ticks()
        
    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.cooldown_time >= self.cooldown:
                self.ready = True

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= self.max_x:
            self.rect.right = self.max_x

    def shoot_laser(self):
        self.laser.add(Laser(self.rect.center, 8, self.rect.bottom))

    def update(self):
        self.get_player_input()
        self.constraint()
        self.recharge()
import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((4,20))
        self.image.fill('red')
        self.rect = self.image.get_rect(midbottom = (0,0))
        self.speed = 8

    def update(self):
        self.rect.y -= self.speed
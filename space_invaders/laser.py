import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((4,20))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = pos)
        self.speed = 8

    def update(self):
        self.rect.y -= self.speed
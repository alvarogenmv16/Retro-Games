import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x, y))


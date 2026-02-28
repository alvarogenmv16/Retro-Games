import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, max_x, speed):
        super().__init__()
        self.image = pygame.image.load('../Graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.max_x = max_x
        self.speed = speed

    def get_player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= self.max_x:
            self.rect.right = self.max_x

    def update(self):
        self.get_player_input()
        self.constraint()
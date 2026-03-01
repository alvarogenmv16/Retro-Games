import pygame, sys
from player import Player

class Game:
    def __init__(self):
        player_sprite = Player((screen_width / 2 ,screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.update()
        self.player.draw(screen)
        self.player.sprite.laser.draw(screen)
        self.player.sprite.laser.update()
        # Update all sprites

# pygame setup
if __name__ == '__main__':
    pygame.init()
    screen_width, screen_height = 600, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True
    game = Game()

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with black
        screen.fill((30,30,30))
        game.run()

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()   
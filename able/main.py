import pygame

from able import interface
from able.interface import Interface


class Main:
    def __init__(self):
        pygame.init()
        self.window_width = 800
        self.window_height = 600
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.interface = Interface()

    def start(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0

    def draw(self):
        self.interface.draw()
        pygame.display.update()


main = Main()
main.start()

import pygame
from game_files.settings import WIDTH, HEIGHT
from game_files.game import Game

class Main:
    @staticmethod
    def start():
        pygame.init()
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("Duck Game")
        game = Game(screen)
        game.run_game()

if __name__ == "__main__":
    Main.start()

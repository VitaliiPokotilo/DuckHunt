import pygame
import sys
import random
from duck import Duck
from game_interface import GameUI
from settings import WIDTH, HEIGHT, FPS, GAME_DURATION, POINTS
from game import Game

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

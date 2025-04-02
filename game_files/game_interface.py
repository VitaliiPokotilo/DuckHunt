import pygame
import sys
import random
from game_files.settings import WIDTH, HEIGHT

class GameUI:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('assetsPhotos/Theme2.png')

        self.font = pygame.font.Font(None, 50)

        self.bar_surface = pygame.Surface((WIDTH, 100))
        self.bar_surface.fill('lightblue')
        self.bar_y = HEIGHT - 100

        self.menu_surface = pygame.Surface((WIDTH, HEIGHT))
        self.menu_surface.fill('lightblue')

        # Кнопки
        self.button_easy = pygame.Rect(212.5, 300, 150, 50)
        self.button_medium = pygame.Rect(362.5, 300, 150, 50)
        self.button_hard = pygame.Rect(512.5, 300, 150, 50)
        self.button_play = pygame.Rect(362.5, 400, 150, 50)
        self.button_exit = pygame.Rect(362.5, 470, 150, 50)

    def draw_game_screen(self, points, remaining_time):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.bar_surface, (0, self.bar_y))

        text_surface = self.font.render(f"Points: {points}", True, 'black')
        self.screen.blit(text_surface, (10, 535))

        text_surface_time = self.font.render(f"Time: {remaining_time}", True, 'black')
        self.screen.blit(text_surface_time, (700, 535))

    def draw_menu(self, points, record, current_speed_factor):
        self.screen.blit(self.menu_surface, (0, 0))
        text_surface = self.font.render("MENU", True, 'White')
        self.screen.blit(text_surface, (390, 100))

        # Кнопки
        pygame.draw.rect(self.screen, 'gray' if current_speed_factor == 0.5 else 'white', self.button_easy)
        pygame.draw.rect(self.screen, 'gray' if current_speed_factor == 1 else 'white', self.button_medium)
        pygame.draw.rect(self.screen, 'gray' if current_speed_factor == 1.5 else 'white', self.button_hard)
        pygame.draw.rect(self.screen, 'white', self.button_play)
        pygame.draw.rect(self.screen, 'white', self.button_exit)

        self.screen.blit(self.font.render("Easy", True, 'black'), (self.button_easy.x + 20, self.button_easy.y + 10))
        self.screen.blit(self.font.render("Medium", True, 'black'), (self.button_medium.x + 10, self.button_medium.y + 10))
        self.screen.blit(self.font.render("Hard", True, 'black'), (self.button_hard.x + 20, self.button_hard.y + 10))
        self.screen.blit(self.font.render("Play", True, 'black'), (self.button_play.x + 20, self.button_play.y + 10))
        self.screen.blit(self.font.render("Exit", True, 'black'), (self.button_exit.x + 30, self.button_exit.y + 10))

        self.screen.blit(self.font.render(f"Your result: {points}", True, 'black'), (330, 170))
        self.screen.blit(self.font.render(f"Your record today: {record}", True, 'black'), (300, 215))

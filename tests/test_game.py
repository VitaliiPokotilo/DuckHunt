import pytest
import pygame
import sys
import os
# Додаємо шлях до кореня проекту до PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_files.game import Game
from game_files.settings import WIDTH, HEIGHT, GAME_DURATION


def test_game_initialization():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(screen)

    assert game.points == 0
    assert game.level == 0
    assert game.run is True
    assert game.current_speed_factor == 1
    assert isinstance(game.duck1, object)
    assert isinstance(game.duck2, object)


def test_handle_mouse_click():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(screen)

    # Імітуємо кнопки меню (бо вони можуть не ініціалізуватися в GameUI)
    game.ui.button_play = pygame.Rect(100, 100, 200, 50)
    game.ui.button_easy = pygame.Rect(100, 200, 200, 50)
    game.ui.button_medium = pygame.Rect(100, 300, 200, 50)
    game.ui.button_hard = pygame.Rect(100, 400, 200, 50)

    game.handle_mouse_click((150, 220))  # Натискання кнопки "Easy"
    assert game.current_speed_factor == 0.5  # Очікуємо зміну швидкості

    game.handle_mouse_click((150, 120))  # Натискання кнопки "Play"
    assert game.level == 1



def test_duck_hit():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(screen)
    game.level = 1

    game.duck1.x = 300
    game.duck1.y = 300
    game.duck2.x = 400
    game.duck2.y = 400

    game.handle_mouse_click((300, 300))
    assert game.points == 1  # Очки збільшуються при попаданні в качку

    game.handle_mouse_click((400, 400))
    assert game.points == 2


def test_update_end_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(screen)

    game.start_time -= GAME_DURATION  # Примусово закінчуємо гру
    game.update()

    assert game.level == 0  # Повернення до меню після завершення гри


def test_exit_button():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(screen)
    game.ui.button_exit = pygame.Rect(100, 300, 200, 50)

    game.handle_mouse_click((150, 320))
    assert game.run is False  # Вихід з гри

    pygame.quit()

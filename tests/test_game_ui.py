import pygame
import pytest
import sys
import os
# Додаємо шлях до кореня проекту до PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game_files.game_interface import GameUI  # Припускаємо, що файл з класом GameUI називається ui.py
from game_files.settings import WIDTH, HEIGHT


def test_game_ui_initialization():
    pygame.init()
    screen = pygame.Surface((WIDTH, HEIGHT))
    game_ui = GameUI(screen)

    assert game_ui.screen == screen
    assert game_ui.background is not None
    assert game_ui.font is not None
    assert game_ui.bar_surface is not None
    assert game_ui.menu_surface is not None


def test_draw_game_screen():
    pygame.init()
    screen = pygame.Surface((WIDTH, HEIGHT))
    game_ui = GameUI(screen)

    points = 10
    remaining_time = 30

    game_ui.draw_game_screen(points, remaining_time)

    # Перевіряємо, що фон та панель інтерфейсу відображаються
    assert screen.get_at((0, 0)) is not None
    assert screen.get_at((WIDTH // 2, HEIGHT - 50)) is not None


def test_draw_menu():
    pygame.init()
    screen = pygame.Surface((WIDTH, HEIGHT))
    game_ui = GameUI(screen)

    points = 15
    record = 50
    current_speed_factor = 1

    game_ui.draw_menu(points, record, current_speed_factor)

    # Перевіряємо, що меню відображається
    assert screen.get_at((WIDTH // 2, HEIGHT // 2)) is not None

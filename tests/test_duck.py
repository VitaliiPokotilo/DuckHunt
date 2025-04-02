# tests/test_duck.py
import sys
import os
import pytest
from pathlib import Path

# Додаємо шлях до кореня проекту для коректного імпорту модулів
sys.path.append(str(Path(__file__).parent.parent))

from game_files.duck import Duck
from game_files.settings import WIDTH, HEIGHT


# Mock-об'єкт для імітації зображення качки
class MockImage:
    def __init__(self):
        self.get_width = lambda: 75  # Фіктивна ширина зображення
        self.get_height = lambda: 75  # Фіктивна висота зображення


# Фікстура, яка створює стандартний об'єкт Duck для тестування
@pytest.fixture
def duck():
    return Duck(
        image=MockImage(),
        x=100,  # Початкова позиція X
        y=100,  # Початкова позиція Y
        speed_x=2,  # Швидкість по горизонталі
        speed_y=1  # Швидкість по вертикалі
    )


def test_duck_initialization(duck):
    """Тестує коректність ініціалізації об'єкта Duck"""
    # Перевіряємо, що параметри ініціалізовані правильно
    assert duck.x == 100
    assert duck.y == 100
    assert duck.speed_x == 2
    assert duck.speed_y == 1


def test_duck_fly_movement(duck):
    """Тестує базовий рух качки без додаткових факторів"""
    initial_x = duck.x
    initial_y = duck.y

    # Викликаємо метод fly з фактором швидкості 1.0
    duck.fly(current_speed_factor=1.0)

    # Перевіряємо, що позиція змінилася відповідно до швидкостей
    assert duck.x == initial_x + duck.speed_x
    assert duck.y == initial_y + duck.speed_y


def test_duck_fly_with_speed_factor(duck):
    """Тестує рух качки з множником швидкості"""
    initial_x = duck.x

    # Викликаємо метод fly з фактором швидкості 2.0
    duck.fly(current_speed_factor=2.0)

    # Перевіряємо, що горизонтальний рух прискорився вдвічі
    assert duck.x == initial_x + duck.speed_x * 2.0


def test_duck_bounce_top_boundary():
    """Тестує відбиття качки від верхньої межі екрану"""
    # Створюємо качку біля верхньої межі, що рухається вгору
    duck = Duck(MockImage(), x=100, y=0, speed_x=2, speed_y=-1)
    duck.fly(current_speed_factor=1.0)

    # Перевіряємо, що вертикальна швидкість змінила напрямок
    assert duck.speed_y == 1


def test_duck_bounce_bottom_boundary():
    """Тестує відбиття качки від нижньої межі екрану"""
    # Створюємо качку біля нижньої межі, що рухається вниз
    duck = Duck(MockImage(), x=100, y=HEIGHT - 200, speed_x=2, speed_y=1)
    duck.fly(current_speed_factor=1.0)

    # Перевіряємо, що вертикальна швидкість змінила напрямок
    assert duck.speed_y == -1


def test_duck_wrap_around_left():
    """Тестує перенесення качки з лівої межі на праву"""
    # Створюємо качку, що вийшла за ліву межу екрану
    duck = Duck(MockImage(), x=-100, y=100, speed_x=-2, speed_y=1)
    duck.fly(current_speed_factor=1.0)

    # Перевіряємо, що качка з'явилася з правого боку
    assert duck.x == WIDTH
    # Нова позиція Y має бути в межах екрану
    assert 0 <= duck.y <= HEIGHT - 200
    # Швидкість по Y має бути або -2, або 2 (випадковий вибір)
    assert duck.speed_y in [-2, 2]


def test_duck_wrap_around_right():
    """Тестує перенесення качки з правої межі на ліву"""
    # Створюємо качку, що вийшла за праву межу екрану
    duck = Duck(MockImage(), x=WIDTH + 1, y=100, speed_x=2, speed_y=1)
    duck.fly(current_speed_factor=1.0)

    # Перевіряємо, що качка з'явилася з лівого боку
    assert duck.x == -50
    # Нова позиція Y має бути в межах екрану
    assert 0 <= duck.y <= HEIGHT - 200
    # Швидкість по Y має бути або -2, або 2 (випадковий вибір)
    assert duck.speed_y in [-2, 2]


def test_duck_random_reset():
    """Тестує випадковість нових координат при перенесенні качки"""
    positions = set()  # Множина для унікальних позицій Y
    speed_ys = set()  # Множина для унікальних швидкостей Y

    # Виконуємо 10 ітерацій для перевірки випадковості
    for _ in range(10):
        duck = Duck(MockImage(), x=-100, y=100, speed_x=-2, speed_y=1)
        duck.fly(current_speed_factor=1.0)
        positions.add(duck.y)
        speed_ys.add(duck.speed_y)

    # Перевіряємо, що отримали різні значення позицій та швидкостей
    assert len(positions) > 1
    assert len(speed_ys) > 1
import pygame
import sys
import random

pygame.init()
fps = 60
timer = pygame.time.Clock()


WIDTH = 875
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Duck Game")
background = pygame.image.load('img/Theme2.png')

duck = pygame.image.load('img/Duck3.png')
duck = pygame.transform.scale(duck, (75, 75))
duck2 = pygame.image.load('img/Duck3inv.png')
duck2 = pygame.transform.scale(duck2, (75, 75))

bar_surface = pygame.Surface((WIDTH, 100))
bar_surface.fill('lightblue')
bar_y = HEIGHT - 100

menu_surface = pygame.Surface((WIDTH, HEIGHT))
menu_surface.fill('lightblue')

button = pygame.Surface((100, 40))
button.fill('White')

font = pygame.font.Font(None, 50)
points = 0

text = f"Points: {points}"
text_surface = font.render(text, True, 'black')
text_rect = text_surface.get_rect(topleft=(10, 535))

game_duration = 30 * 1000  # Час у мілісекундах (30 секунд)
start_time = pygame.time.get_ticks()  # Початковий час

duck1_x = WIDTH
duck1_y = random.randint(0, HEIGHT - 200)
duck1_speed_x = -5
duck1_speed_y = random.choice([-2, 2])

duck2_x = -50
duck2_y = random.randint(0, HEIGHT - 200)
duck2_speed_x = 5
duck2_speed_y = random.choice([-2, 2])

# Рівні складності
level = 0
current_speed_factor = 1


# Кнопки для вибору рівнів
button_easy = pygame.Rect(212.5, 300, 150, 50)
button_medium = pygame.Rect(362.5, 300, 150, 50)
button_hard = pygame.Rect(512.5, 300, 150, 50)
button_play = pygame.Rect(362.5, 400, 150, 50)

# Функції для руху качок
def fly_duck1():
    global duck1_x, duck1_y, duck1_speed_y

    duck1_x += duck1_speed_x * current_speed_factor
    duck1_y += duck1_speed_y

    if duck1_y <= 0 or duck1_y >= HEIGHT - 200:
        duck1_speed_y *= -1

    if duck1_x + 75 < 0:
        duck1_x = WIDTH
        duck1_y = random.randint(0, HEIGHT - 200)
        duck1_speed_y = random.choice([-2, 2])

def fly_duck2():
    global duck2_x, duck2_y, duck2_speed_y

    duck2_x += duck2_speed_x * current_speed_factor
    duck2_y += duck2_speed_y

    if duck2_y <= 0 or duck2_y >= HEIGHT - 200:
        duck2_speed_y *= -1

    if duck2_x > WIDTH:
        duck2_x = -50
        duck2_y = random.randint(0, HEIGHT - 200)
        duck2_speed_y = random.choice([-2, 2])

# Основний цикл гри
run = True
while run:
    timer.tick(fps)
    screen.fill('black')

    if level == 1:

        # Оновлення тексту з кількістю балів
        text = f"Points: {points}"
        text_surface = font.render(text, True, 'black')

        # Оновлення тексту з таймером
        elapsed_time = pygame.time.get_ticks() - start_time
        remaining_time = max((game_duration - elapsed_time) // 1000, 0)  # Час у секундах
        if elapsed_time >= game_duration:  # Перевірка, чи час вичерпано
            level = 0


        text_time = f"Time: {remaining_time}"
        text_surface_time = font.render(text_time, True, 'black')
        text_rect_time = text_surface_time.get_rect(topleft=(700, 535))

        # Відображення графіки
        screen.blit(background, (0, 0))
        screen.blit(bar_surface, (0, bar_y))
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface_time, text_rect_time)

        # Рух качок
        fly_duck1()
        screen.blit(duck, (duck1_x, duck1_y))
        duck1_rect = duck.get_rect(topleft=(duck1_x, duck1_y))

        fly_duck2()
        screen.blit(duck2, (duck2_x, duck2_y))
        duck2_rect = duck2.get_rect(topleft=(duck2_x, duck2_y))
    elif level == 0:

        # Меню
        screen.blit(menu_surface, (0, 0))
        text = f"MENU"
        text_surface = font.render(text, True, 'White')
        screen.blit(text_surface, (390, 100))

        # Качки у меню
        screen.blit(duck, (415, 30))
        screen.blit(duck, (340, 80))
        screen.blit(duck, (480, 70))

        # Відображення кнопок рівнів
        pygame.draw.rect(screen, 'gray' if current_speed_factor == 0.5 else 'white', button_easy)
        pygame.draw.rect(screen, 'gray' if current_speed_factor == 1 else 'white', button_medium)
        pygame.draw.rect(screen, 'gray' if current_speed_factor == 1.5 else 'white', button_hard)
        easy_text = font.render("Easy", True, 'black')
        medium_text = font.render("Medium", True, 'black')
        hard_text = font.render("Hard", True, 'black')
        screen.blit(easy_text, (button_easy.x + 20, button_easy.y + 10))
        screen.blit(medium_text, (button_medium.x + 10, button_medium.y + 10))
        screen.blit(hard_text, (button_hard.x + 20, button_hard.y + 10))

        pygame.draw.rect(screen, 'white', button_play)
        play_text = font.render("Play", True, 'black')
        screen.blit(play_text, (button_play.x + 20, button_play.y + 10))

        text = f"Your result: {points}"
        text_surface = font.render(text, True, 'black')
        screen.blit(text_surface, text_surface.get_rect(topleft=(330, 170)))






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if level == 1:
                if duck1_rect.collidepoint(event.pos):
                    duck1_x = WIDTH
                    duck1_y = random.randint(0, HEIGHT - 200)
                    points += 1

                if duck2_rect.collidepoint(event.pos):
                    duck2_x = -50
                    duck2_y = random.randint(0, HEIGHT - 200)
                    points += 1
            elif level == 0:
                if button_easy.collidepoint(event.pos):
                    current_speed_factor = 0.5
                elif button_medium.collidepoint(event.pos):
                    current_speed_factor = 1
                elif button_hard.collidepoint(event.pos):
                    current_speed_factor = 1.5
                if button_play.collidepoint(event.pos):
                    points = 0
                    start_time = pygame.time.get_ticks()
                    level = 1

    pygame.display.flip()

pygame.quit()

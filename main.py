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


duck1_x = WIDTH
duck1_y = random.randint(0, HEIGHT - 200)
duck1_speed_x = -5
duck1_speed_y = random.choice([-2, 2])

duck2_x = -50
duck2_y = random.randint(0, HEIGHT - 200)
duck2_speed_x = 5
duck2_speed_y = random.choice([-2, 2])

# Рівні складності
level = 1
current_speed_factor = 1




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








        # Відображення графіки
        screen.blit(background, (0, 0))
        screen.blit(bar_surface, (0, bar_y))


        # Рух качок
        fly_duck1()
        screen.blit(duck, (duck1_x, duck1_y))
        duck1_rect = duck.get_rect(topleft=(duck1_x, duck1_y))

        fly_duck2()
        screen.blit(duck2, (duck2_x, duck2_y))
        duck2_rect = duck2.get_rect(topleft=(duck2_x, duck2_y))






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if level == 1:
                if duck1_rect.collidepoint(event.pos):
                    duck1_x = WIDTH
                    duck1_y = random.randint(0, HEIGHT - 200)


                if duck2_rect.collidepoint(event.pos):
                    duck2_x = -50
                    duck2_y = random.randint(0, HEIGHT - 200)



    pygame.display.flip()

pygame.quit()

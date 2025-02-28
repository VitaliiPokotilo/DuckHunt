import pygame
import sys
import random
from duck import Duck
from game_interface import GameUI
from settings import WIDTH, HEIGHT

pygame.init()
fps = 60
timer = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Duck Game")


# Основна гра
ui = GameUI(screen)
duck_img = pygame.image.load('assets/Duck3.png')
duck_img = pygame.transform.scale(duck_img, (75, 75))

duck_img_inv = pygame.image.load('assets/Duck3inv.png')
duck_img_inv = pygame.transform.scale(duck_img_inv, (75, 75))

duck1 = Duck(duck_img, WIDTH, random.randint(0, HEIGHT - 200), -5, random.choice([-2, 2]))
duck2 = Duck(duck_img_inv, -50, random.randint(0, HEIGHT - 200), 5, random.choice([-2, 2]))

game_duration = 30 * 1000
start_time = pygame.time.get_ticks()
points = 0
record = 0
level = 0
current_speed_factor = 1

run = True
while run:
    timer.tick(fps)
    screen.fill('black')

    if level == 1:
        elapsed_time = pygame.time.get_ticks() - start_time
        remaining_time = max((game_duration - elapsed_time) // 1000, 0)

        if elapsed_time >= game_duration:
            level = 0

        ui.draw_game_screen(points, remaining_time)

        duck1.fly(current_speed_factor)
        screen.blit(duck1.image, (duck1.x, duck1.y))
        duck1_rect = duck1.image.get_rect(topleft=(duck1.x, duck1.y))

        duck2.fly(current_speed_factor)
        screen.blit(duck2.image, (duck2.x, duck2.y))
        duck2_rect = duck2.image.get_rect(topleft=(duck2.x, duck2.y))

    elif level == 0:
        if points > record:
            record = points

        ui.draw_menu(points, record, current_speed_factor)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if level == 1:
                if duck1_rect.collidepoint(event.pos):
                    duck1.x = WIDTH
                    duck1.y = random.randint(0, HEIGHT - 200)
                    points += 1
                if duck2_rect.collidepoint(event.pos):
                    duck2.x = -50
                    duck2.y = random.randint(0, HEIGHT - 200)
                    points += 1
            elif level == 0:
                if ui.button_easy.collidepoint(event.pos):
                    current_speed_factor = 0.5
                elif ui.button_medium.collidepoint(event.pos):
                    current_speed_factor = 1
                elif ui.button_hard.collidepoint(event.pos):
                    current_speed_factor = 1.5
                if ui.button_play.collidepoint(event.pos):
                    points = 0
                    start_time = pygame.time.get_ticks()
                    level = 1
                elif ui.button_exit.collidepoint(event.pos):
                    run = False

    pygame.display.flip()

pygame.quit()

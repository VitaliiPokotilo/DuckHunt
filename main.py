import pygame
import sys
import random
from duck import Duck

pygame.init()
fps = 60
timer = pygame.time.Clock()

WIDTH = 875
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])

pygame.display.set_caption("Duck Game")
background = pygame.image.load('assets/Theme2.png')

duck = pygame.image.load('assets/Duck3.png')
duck = pygame.transform.scale(duck, (75, 75))

duck2 = pygame.image.load('assets/Duck3inv.png')
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
record = 0
text = f"Points: {points}"
text_surface = font.render(text, True, 'black')
text_rect = text_surface.get_rect(topleft=(10, 535))

game_duration = 30 * 1000  # Time in milliseconds (30 seconds)
start_time = pygame.time.get_ticks()  # Starting time

# Duck class


# Duck instances
duck1 = Duck(duck, WIDTH, random.randint(0, HEIGHT - 200), -5, random.choice([-2, 2]))
duck2 = Duck(duck2, -50, random.randint(0, HEIGHT - 200), 5, random.choice([-2, 2]))

# Difficulty levels
level = 0
current_speed_factor = 1

# Buttons for selecting levels
button_easy = pygame.Rect(212.5, 300, 150, 50)
button_medium = pygame.Rect(362.5, 300, 150, 50)
button_hard = pygame.Rect(512.5, 300, 150, 50)
button_play = pygame.Rect(362.5, 400, 150, 50)
button_exit = pygame.Rect(362.5, 470, 150, 50)

# Main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('black')

    if level == 1:
        # Update points text
        text = f"Points: {points}"
        text_surface = font.render(text, True, 'black')

        # Update timer text
        elapsed_time = pygame.time.get_ticks() - start_time
        remaining_time = max((game_duration - elapsed_time) // 1000, 0)  # Time in seconds
        if elapsed_time >= game_duration:  # Check if time is up
            level = 0

        text_time = f"Time: {remaining_time}"
        text_surface_time = font.render(text_time, True, 'black')
        text_rect_time = text_surface_time.get_rect(topleft=(700, 535))

        # Display graphics
        screen.blit(background, (0, 0))
        screen.blit(bar_surface, (0, bar_y))
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface_time, text_rect_time)

        # Move ducks
        duck1.fly(current_speed_factor)
        screen.blit(duck1.image, (duck1.x, duck1.y))
        duck1_rect = duck1.image.get_rect(topleft=(duck1.x, duck1.y))

        duck2.fly(current_speed_factor)
        screen.blit(duck2.image, (duck2.x, duck2.y))
        duck2_rect = duck2.image.get_rect(topleft=(duck2.x, duck2.y))

    elif level == 0:
        if points > record:
            record = points

        # Menu
        screen.blit(menu_surface, (0, 0))
        text = f"MENU"
        text_surface = font.render(text, True, 'White')
        screen.blit(text_surface, (390, 100))

        # Ducks in menu
        screen.blit(duck, (415, 30))
        screen.blit(duck, (340, 80))
        screen.blit(duck, (480, 70))

        # Display level buttons
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
        text_record = f"Your record today: {record}"
        text_surface_record = font.render(text_record, True, 'black')
        screen.blit(text_surface_record, text_surface_record.get_rect(topleft=(300, 215)))
        pygame.draw.rect(screen, 'white', button_exit)
        exit_text = font.render("Exit", True, 'black')
        screen.blit(exit_text, (button_exit.x + 30, button_exit.y + 10))

    # Event handling
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
                elif button_exit.collidepoint(event.pos):  # Перенесено всередину MOUSEBUTTONDOWN
                    run = False
    pygame.display.flip()

pygame.quit()
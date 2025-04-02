import pygame
import sys
import random
from duck import Duck
from game_interface import GameUI
from settings import WIDTH, HEIGHT, FPS, GAME_DURATION, POINTS


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.timer = pygame.time.Clock()
        self.ui = GameUI(screen)
        self.duck_img = pygame.transform.scale(pygame.image.load('assetsPhotos/Duck3.png'), (75, 75))
        self.duck_img_inv = pygame.transform.scale(pygame.image.load('assetsPhotos/Duck3inv.png'), (75, 75))

        self.duck1 = Duck(self.duck_img, WIDTH, random.randint(0, HEIGHT - 200), -5, random.choice([-2, 2]))
        self.duck2 = Duck(self.duck_img_inv, -50, random.randint(0, HEIGHT - 200), 5, random.choice([-2, 2]))

        self.start_time = pygame.time.get_ticks()
        self.points = POINTS
        self.record = 0
        self.level = 0
        self.current_speed_factor = 1
        self.run = True

        # Завантажуємо музику для головного меню
        pygame.mixer.music.load('assetsAudio/title_screen.mp3')
        pygame.mixer.music.play(-1, 0.0)  # -1 означає, що музика буде грати в циклі

        # Завантаження звуків
        self.hit_sound = pygame.mixer.Sound('assetsAudio/Quack.mp3')
        self.shot_sound = pygame.mixer.Sound('assetsAudio/Hit.mp3')

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event.pos)
                self.shot_sound.play()  # Відтворюємо звук пострілу при натисканні миші

    def handle_mouse_click(self, pos):
        if self.level == 1:
            if self.duck1.image.get_rect(topleft=(self.duck1.x, self.duck1.y)).collidepoint(pos):
                self.duck1.x = WIDTH
                self.duck1.y = random.randint(0, HEIGHT - 200)
                self.points += 1
                self.hit_sound.play()  # Відтворюємо звук при влучанні в качку
            if self.duck2.image.get_rect(topleft=(self.duck2.x, self.duck2.y)).collidepoint(pos):
                self.duck2.x = -50
                self.duck2.y = random.randint(0, HEIGHT - 200)
                self.points += 1
                self.hit_sound.play()  # Відтворюємо звук при влучанні в качку
        elif self.level == 0:
            if self.ui.button_easy.collidepoint(pos):
                self.current_speed_factor = 0.5
            elif self.ui.button_medium.collidepoint(pos):
                self.current_speed_factor = 1
            elif self.ui.button_hard.collidepoint(pos):
                self.current_speed_factor = 1.5
            if self.ui.button_play.collidepoint(pos):
                self.points = 0
                self.start_time = pygame.time.get_ticks()
                self.level = 1

                # Заміна музики для рівня гри
                pygame.mixer.music.load('assetsAudio/Game.mp3')
                pygame.mixer.music.play(-1, 0.0)  # Грає в циклі

            elif self.ui.button_exit.collidepoint(pos):
                self.run = False

    def update(self):
        self.timer.tick(FPS)
        self.screen.fill('black')

        if self.level == 1:
            elapsed_time = pygame.time.get_ticks() - self.start_time
            remaining_time = max((GAME_DURATION - elapsed_time) // 1000, 0)

            if elapsed_time >= GAME_DURATION:
                self.level = 0

                # Повертаємо музику до меню після закінчення гри
                pygame.mixer.music.load('assetsAudio/title_screen.mp3')
                pygame.mixer.music.play(-1, 0.0)  # Знову музика для головного меню

            self.ui.draw_game_screen(self.points, remaining_time)
            self.duck1.fly(self.current_speed_factor)
            self.screen.blit(self.duck1.image, (self.duck1.x, self.duck1.y))
            self.duck2.fly(self.current_speed_factor)
            self.screen.blit(self.duck2.image, (self.duck2.x, self.duck2.y))
        else:
            if self.points > self.record:
                self.record = self.points
            self.ui.draw_menu(self.points, self.record, self.current_speed_factor)

        pygame.display.flip()

    def run_game(self):
        while self.run:
            self.handle_events()
            self.update()
        pygame.quit()

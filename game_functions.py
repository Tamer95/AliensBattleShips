import sys
import pygame
from gun import Gun


def check_events(gun):
    """обрабатывает нажатие клавиш и событий мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.moving_right = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                gun.moving_left = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.moving_right = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                gun.moving_left = False


def update_screen(ai_settings, screen, gun):
    """Обновляет изображее на экране и отображает новый экран"""
    # При каждом проходе цикла перерисовывает экран
    screen.fill(ai_settings.bg_color)
    gun.blit()
    # отображение последнего прорисованного экрана
    pygame.display.flip()

import sys
import pygame


def check_events():
    """обрабатывает нажатие клавиш и событий мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

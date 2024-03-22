import pygame
from settings_alien import Settings # настройки корабля, цвет фона и т.д
from gun import Gun # сам карабль
from game_functions import check_events as gf # тут проверка экрана на события
from game_functions import update_screen  # тут постоянное обновление экрана


def run_game():
    """Инициализирует игру и создает объкт экрана"""
    pygame.init()  # для подгрузги всех остальных зависимостей
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    gun = Gun(screen)  # отрисовка пушки после импорта

    # Запуск основного цикла
    while True:
        gf(gun)
        gun.update()
        update_screen(ai_settings, screen, gun)




run_game()

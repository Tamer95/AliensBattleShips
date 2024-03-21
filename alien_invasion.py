import sys
import pygame
from settings_alien import Settings
from gun import Gun


def run_game():
    """Инициализирует игру и создает объкт экрана"""
    pygame.init()  # для подгрузги всех остальных зависимостей
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    gun = Gun(screen)  # отрисовка пушки после импорта

    # Запуск основного цикла
    while True:
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():  # отслеживает движение пользователя по экрану (клавиатура, мышь)
            if event.type == pygame.QUIT:  # если пользователь нажал красный крестик на углу экрана то, выход
                sys.exit()

        # screen.fill(ai_settings.bg_color)
        pygame.display.flip() # flip() отобразит последний отрисованый экран со стиранием старого
        gun.output()


run_game()

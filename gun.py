import pygame


class Gun:
    def __init__(self, screen):
        """инициализация экрана пушки"""
        self.screen = screen  # сам экран
        self.image = pygame.image.load('images/spaceship.png')  # загрузка фото корабля
        self.rect = self.image.get_rect()  # распалогаем пушку на объекте в виде квадрата
        self.screen_rect = screen.get_rect()  # получаем квадратный объект
        self.rect.centerx = self.screen_rect.centerx  # координаты пушки
        self.rect.bottom = self.screen_rect.bottom  # координаты низа пушки
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учётом флага"""
        if self.moving_right:
            # переместить корабль по одному позицию вправо
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1



    def blit(self):
        """рисуем пушку"""
        self.screen.blit(self.image, self.rect)  # метот blit() отрисовывает то есть  всегда обновляет экран

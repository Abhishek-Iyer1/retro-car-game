import pygame

from pygame import Surface
from global_values import *

class Player ():
    def __init__(self, screen: Surface, spawn_coords: list[int]):
        self.rect = pygame.draw.rect(screen, RED, spawn_coords, border_radius=20)
        self.x = self.rect.centerx
        self.left = self.rect.left
        self.y = self.rect.centery
        self.right = self.rect.right
        self.top = self.rect.top
        self.bottom = self.rect.bottom
        
    def move_left(self):
        # while isMoving == True:
            self.rect.move_ip(-INCR_HOR, 0)
        # self.rect.update(self.rect)

    def move_right(self):
        # while isMoving == True:
            self.rect.move_ip(INCR_HOR, 0)

    def move_up(self):
        # while isMoving == True:
            self.rect.move_ip(0, -INCR_VER)

    def move_down(self):
        # while isMoving == True:
            self.rect.move_ip(0, INCR_VER)

    def update(self, screen):
        self.x = self.rect.centerx
        self.left = self.rect.left
        self.y = self.rect.centery
        self.right = self.rect.right
        self.top = self.rect.top
        self.bottom = self.rect.bottom
        pygame.draw.rect(screen, RED, self.rect, border_radius=20)

    def destroy_player():
        pass

class Meter():
    def __init__(self, screen: Surface, spawn_coords = list[int]):
        self.meter_graphic = pygame.draw.rect(screen, RED, spawn_coords, border_radius= 10)
        self.outline = pygame.draw.rect(screen, BLACK, spawn_coords, 5, 10)
        self.value = 100

    def leak(self, time_elapsed_since_fuel_leak):
        if time_elapsed_since_fuel_leak > 1000:
            self.move(-10)
            time_elapsed_since_fuel_leak = 0
        return time_elapsed_since_fuel_leak
    def move(self, value: float):
        self.value += value
        self.meter_graphic.h += value
        self.meter_graphic.top -= value

    def update(self, screen: Surface):
        pygame.draw.rect(screen, RED, self.meter_graphic, border_radius=10)
        pygame.draw.rect(screen, BLACK, self.outline, 5, 10)

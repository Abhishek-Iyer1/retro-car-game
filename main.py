import pygame
import random

from global_values import *
from player import Player, Meter, FuelBox
from utils import *

pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project 0")
exit = False

# Instantiate basic screen
paint_game_screen(screen)

# Instantiate player
player = Player(screen, [450, 425, 100, 150])

# Istantiate Fuel Meter
fuel_meter = Meter(screen, [900, 100, 20, 100])

# Instantiate Fuel Box 
fuel_box = FuelBox(screen, [275, 50, 50, 50])

# Define constants
time_elapsed_since_fuel_leak = 0
time_elapsed_since_fuel_box = 0
time_elapsed_since_last_move = 0
game_over = False

#Instantiate clock
clock = pygame.time.Clock()
fuel_clock = pygame.time.Clock()
fuel_box_clock = pygame.time.Clock()
movement_clock = pygame.time.Clock()


#Game begins, update loop
while not exit:
    # print(f"GAME OVER: {game_over}")
    if not game_over:
        print(f"Fuel Meter: {fuel_meter.value}")
        game_over = check_if_game_over(screen, fuel_meter)
        time_elapsed_since_fuel_leak, time_elapsed_since_fuel_box, time_elapsed_since_last_move = handle_additional_clocks([fuel_clock, fuel_box_clock, movement_clock], time_elapsed_since_fuel_leak, time_elapsed_since_fuel_box, time_elapsed_since_last_move)
        moveLeft = False; moveRight = False; moveUp = False; moveDown = False
        # Handle all events while game is ongoing
        for event in pygame.event.get():
            # print(f"Event: {event}")

            # Exit case: When cross is pressed, exit status is updated, game is quit
            if event.type == pygame.QUIT:
                exit = True
            
            move_status: list[bool] = handle_event(event)
        
        handle_movement(move_status, player)
        rects = screen.get_rect()
        print(f"RECTS: {rects}")
        time_elapsed_since_fuel_leak = fuel_meter.leak(time_elapsed_since_fuel_leak)

        if time_elapsed_since_fuel_box > 10000:
            spawn_coords_fuel_box = [random.choice([275, 475, 675]), 50, 50, 50]
            fuel_box.spawn(screen, spawn_coords_fuel_box)
            fuel_box.destroyed = False
            fuel_box.value = 50
            time_elapsed_since_fuel_box = 0

        if time_elapsed_since_last_move > 200:
            fuel_box.move(time_elapsed_since_last_move)
            time_elapsed_since_last_move = 0

        check_player_fuelbox(player, fuel_box, fuel_meter)
        paint_game_screen(screen)
        player.update(screen)
        fuel_meter.update(screen)
        fuel_box.update(screen)
        pygame.display.flip()
        clock.tick(FPS)
    else:
        paint_game_over_screen(screen)
        # Handle all events while game is ongoing
        for event in pygame.event.get():
            # print(f"Event: {event}")

            # Exit case: When cross is pressed, exit status is updated, game is quit
            if event.type == pygame.QUIT:
                exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == K_KP_ENTER:
                    game_over = False
                    fuel_meter = Meter(screen, [900, 100, 20, 100])
                    fuel_box.destroyed = True
                    # print(game_over)
        
        pygame.display.flip()
        clock.tick(FPS)

            